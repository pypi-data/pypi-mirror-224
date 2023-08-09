r"""
                                                             
  _____/ ____\______ ________________    ____   ___________ 
 /  _ \   __\/  ___// ___\_  __ \__  \  /  _ \_/ __ \_  __ \
(  <_> )  |  \___ \\  \___|  | \// __ \(  <_> )  ___/|  | \/
 \____/|__| /____  >\___  >__|  (____  /\____/ \___  >__|   
                 \/     \/           \/            \/         
"""
import time
import asyncio
import logging
import ssl
import certifi
import contextvars
import math
from diskcache import Cache
from tenacity import retry,stop_after_attempt,wait_random,retry_if_not_exception_type
from rich.progress import Progress
from rich.progress import (
    Progress,
    TextColumn,
    SpinnerColumn
)
from rich.panel import Panel
from rich.console import Group
from rich.live import Live
from rich.style import Style
import arrow
import ofscraper.constants as constants
from ofscraper.utils.semaphoreDelayed import semaphoreDelayed
from ..utils import auth
from ..utils.paths import getcachepath
import ofscraper.utils.console as console
import ofscraper.utils.args as args_
import ofscraper.classes.sessionbuilder as sessionbuilder

log=logging.getLogger("shared")
attempt = contextvars.ContextVar("attempt")

sem = semaphoreDelayed(constants.MAX_SEMAPHORE)
@retry(retry=retry_if_not_exception_type(KeyboardInterrupt),stop=stop_after_attempt(constants.NUM_TRIES),wait=wait_random(min=constants.OF_MIN, max=constants.OF_MAX),reraise=True)   
async def scrape_timeline_posts(c, model_id,progress, timestamp=None,required_ids=None) -> list:
    global tasks
    global sem
    posts=None
    attempt.set(attempt.get(0) + 1)
    if timestamp and   (float(timestamp)>(args_.getargs().before or arrow.now()).float_timestamp):
        return []
    if timestamp:
        log.debug(arrow.get(math.trunc(float(timestamp))))
        timestamp=str(timestamp)
        ep = constants.timelineNextEP
        url = ep.format(model_id, timestamp)
    else:
        ep=constants.timelineEP
        url=ep.format(model_id)
    log.debug(url)
    async with sem:
        task=progress.add_task(f"Attempt {attempt.get()}/{constants.NUM_TRIES}: Timestamp -> {arrow.get(math.trunc(float(timestamp))) if timestamp!=None  else 'initial'}",visible=True)
        async with  c.requests(url=url)() as r:
            if r.ok:
                progress.remove_task(task)
                posts = (await r.json_())['list']
                log_id=f"timestamp:{arrow.get(math.trunc(float(timestamp))) if timestamp!=None  else 'initial'}"
                if not posts:
                    posts= []
                if len(posts)==0:
                    log.debug(f"{log_id} -> number of post found 0")


                elif len(posts)>0:
                    log.debug(f"{log_id} -> number of post found {len(posts)}")
                    log.debug(f"{log_id} -> first date {posts[0].get('createdAt') or posts[0].get('postedAt')}")
                    log.debug(f"{log_id} -> last date {posts[-1].get('createdAt') or posts[-1].get('postedAt')}")
                    log.debug(f"{log_id} -> found postids {list(map(lambda x:x.get('id'),posts))}")
                    log.trace("{log_id} -> post raw {posts}".format(log_id=log_id,posts=  "\n\n".join(list(map(lambda x:f"scrapeinfo timeline: {str(x)}",posts)))))
                               
                    if required_ids==None:
                        attempt.set(0)
                        tasks.append(asyncio.create_task(scrape_timeline_posts(c, model_id,progress,timestamp=posts[-1]['postedAtPrecise'])))
                    else:
                        [required_ids.discard(float(ele["postedAtPrecise"])) for ele in posts]
                        #try once more to get id if only 1 left
                        if len(required_ids)==1:
                            attempt.set(0)
                            tasks.append(asyncio.create_task(scrape_timeline_posts(c, model_id,progress,timestamp=posts[-1]['postedAtPrecise'],required_ids=set())))

                        elif len(required_ids)>0:
                            attempt.set(0)
                            tasks.append(asyncio.create_task(scrape_timeline_posts(c, model_id,progress,timestamp=posts[-1]['postedAtPrecise'],required_ids=required_ids)))
            else:
                    log.debug(f"[bold]timeline response status code:[/bold]{r.status}")
                    log.debug(f"[bold]timeline response:[/bold] {await r.text_()}")
                    log.debug(f"[bold]timeline headers:[/bold] {r.headers}")

                    progress.remove_task(task)
                    r.raise_for_status()
    return posts



async def get_timeline_post(model_id): 
    
    overall_progress=Progress(SpinnerColumn(style=Style(color="blue")),TextColumn("Getting timeline media...\n{task.description}"))
    job_progress=Progress("{task.description}")
    progress_group = Group(
    overall_progress,
    Panel(Group(job_progress)))

    global tasks
    tasks=[]
    min_posts=50
    responseArray=[]
    page_count=0
    
    with Live(progress_group, refresh_per_second=5,console=console.get_shared_console()): 
        async with sessionbuilder.sessionBuilder() as c:
            cache = Cache(getcachepath())
            oldtimeline=cache.get(f"timeline_{model_id}",default=[]) if not args_.getargs().no_cache else []
            log.trace("oldtimeline {posts}".format(posts=  "\n\n".join(list(map(lambda x:f"oldtimeline: {str(x)}",oldtimeline)))))

            oldtimeset=set(map(lambda x:x.get("id"),oldtimeline))
            log.debug(f"[bold]Timeline Cache[/bold] {len(oldtimeline)} found")
            oldtimeline=list(filter(lambda x:x.get("postedAtPrecise")!=None,oldtimeline))
            postedAtArray=sorted(list(map(lambda x:float(x["postedAtPrecise"]),oldtimeline)))
            filteredArray=list(filter(lambda x:x>=(args_.getargs().after or arrow.get(0)).float_timestamp,postedAtArray))
            
        
        
            if len(filteredArray)>min_posts:
                splitArrays=[filteredArray[i:i+min_posts] for i in range(0, len(filteredArray), min_posts)]
                #use the previous split for timesamp
                tasks.append(asyncio.create_task(scrape_timeline_posts(c,model_id,job_progress,required_ids=set(splitArrays[0]),timestamp= args_.getargs().after.float_timestamp if args_.getargs().after else None)))
                [tasks.append(asyncio.create_task(scrape_timeline_posts(c,model_id,job_progress,required_ids=set(splitArrays[i]),timestamp=splitArrays[i-1][-1])))
                for i in range(1,len(splitArrays)-1)]
                # keeping grabbing until nothign left
                tasks.append(asyncio.create_task(scrape_timeline_posts(c,model_id,job_progress,timestamp=splitArrays[-2][-1])))
            else:
                tasks.append(asyncio.create_task(scrape_timeline_posts(c,model_id,job_progress,timestamp=args_.getargs().after.float_timestamp if args_.getargs().after else None)))
        

            page_task = overall_progress.add_task(f' Pages Progress: {page_count}',visible=True)
            while len(tasks)!=0:
                for coro in asyncio.as_completed(tasks):
                    result=await coro or []
                    page_count=page_count+1
                    overall_progress.update(page_task,description=f'Pages Progress: {page_count}')
                    responseArray.extend(result)
                time.sleep(1)
                tasks=list(filter(lambda x:x.done()==False,tasks))
            overall_progress.remove_task(page_task)
    unduped=[]
    dupeSet=set()
    log.debug(f"[bold]Timeline Count with Dupes[/bold] {len(responseArray)} found")
    for post in responseArray:
        if post["id"] in dupeSet:
            continue
        dupeSet.add(post["id"])
        oldtimeset.discard(post["id"])
        unduped.append(post)
    log.trace(f"timeline dupeset postids {dupeSet}")
    log.trace("post raw unduped {posts}".format(posts=  "\n\n".join(list(map(lambda x:f"undupedinfo timeline: {str(x)}",unduped)))))
    log.debug(f"[bold]Timeline Count without Dupes[/bold] {len(unduped)} found")
    if len(oldtimeset)==0 and not (args_.getargs().before or args_.getargs().after):
        cache.set(f"timeline_{model_id}",list(map(lambda x:{"id":x.get("id"),"postedAtPrecise":x.get("postedAtPrecise")},unduped)),expire=constants.RESPONSE_EXPIRY)
        cache.set(f"timeline_check_{model_id}",unduped,expire=constants.CHECK_EXPIRY)
        cache.close()
    elif len(oldtimeset)>0 and not (args_.getargs().before or args_.getargs().after):
        cache.set(f"timeline_{model_id}",[],expire=constants.RESPONSE_EXPIRY)
        cache.set(f"timeline_check_{model_id}",[],expire=constants.CHECK_EXPIRY)

        cache.close()
        log.debug("Some post where not retrived resetting cache")
    return unduped                                


def get_individual_post(id,c=None):
    with c.requests(constants.INDVIDUAL_TIMELINE.format(id))() as r:
        if r.ok:
            log.trace(f"message raw individual {r.json()}")
            return r.json()
        else:
            log.debug(f"[bold]individual post response status code:[/bold]{r.status}")
            log.debug(f"[bold]individual post response:[/bold] {r.text_()}")
            log.debug(f"[bold]individual post headers:[/bold] {r.headers}")


