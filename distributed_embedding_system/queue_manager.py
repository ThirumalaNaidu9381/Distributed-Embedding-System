from queue import Queue

# Producer -> Consumer Queue
job_queue = Queue()


def enqueue(job):
    job_queue.put(job)


def dequeue():
    return job_queue.get()


def task_done():
    job_queue.task_done()