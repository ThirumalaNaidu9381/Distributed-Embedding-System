from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class JobStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class EmbeddingRequest(BaseModel):
    text: str


class Job(BaseModel):
    job_id: str
    text: str
    status: JobStatus
    embedding: Optional[List[float]] = None