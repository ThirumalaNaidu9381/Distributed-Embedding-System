from uuid import uuid4

from fastapi import FastAPI, HTTPException

from models import Job, JobStatus, EmbeddingRequest
from job_store import jobs
from queue_manager import enqueue

app = FastAPI(title="Distributed Embedding System")


@app.post("/embeddings")
def create_embedding_job(request: EmbeddingRequest):

    job_id = str(uuid4())

    job = Job(
        job_id=job_id,
        text=request.text,
        status=JobStatus.PENDING
    )

    jobs[job_id] = job

    enqueue(job)

    return {
        "job_id": job_id,
        "status": job.status
    }


@app.get("/jobs/{job_id}")
def get_job(job_id: str):

    job = jobs.get(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


@app.get("/health")
def health():

    return {
        "status": "UP"
    }