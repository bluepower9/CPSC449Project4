import httpx

# enqueue a job containing score
def add_to_queue(result):
    r = httpx.post('http://localhost:5400/leaderboard/update', data=result)
    return r