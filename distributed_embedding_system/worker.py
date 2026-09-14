from embedding_service import EmbeddingService
from job_store import jobs
from models import JobStatus
from queue_manager import dequeue, task_done
from vector_store import vector_store


print("Worker started...")


while True:

    job = dequeue()

    try:

        print(f"Processing Job : {job.job_id}")

        job.status = JobStatus.PROCESSING

        embedding = EmbeddingService.generate_embedding(
            job.text
        )

        vector_store.store(
            job.job_id,
            embedding
        )

        job.embedding = embedding

        job.status = JobStatus.COMPLETED

        jobs[job.job_id] = job

        print(f"Completed : {job.job_id}")

    except Exception as e:

        print(e)

        job.status = JobStatus.FAILED

        jobs[job.job_id] = job

    finally:

        task_done()