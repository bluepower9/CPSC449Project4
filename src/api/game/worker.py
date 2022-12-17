from rq import Queue
from rq.job import Job
from rq.registry import FailedJobRegistry
from redis import Redis
from job import add_to_queue
import time

async def worker(data):
    # worker to send score to leaderboard service
    redis_connection = Redis()
    registry = FailedJobRegistry(queue=q)
    q = Queue('high', connection=redis_connection)
    job = q.enqueue(add_to_queue, data)
    time.sleep(2)

    # show all failed job IDs and the exceptions they caused during runtime
    for job_id in registry.get_job_ids():
        job = Job.fetch(job_id, connection=redis_connection)
        print(job_id, job.exc_info)