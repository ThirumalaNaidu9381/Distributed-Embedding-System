Distributed Embedding System (MVP)
Install
pip install -r requirements.txt
Terminal 1
Run Worker

python worker.py
Terminal 2
Run API

uvicorn app:app --reload
Open
http://127.0.0.1:8000/docs
Create Job
POST

/embeddings
Body

{
  "text": "Hello World"
}
Response

{
  "job_id":"....",
  "status":"PENDING"
}
Check Status
GET

/jobs/{job_id}
Initially

{
    "status":"PENDING"
}
After worker completes

{
    "job_id":"...",
    "status":"COMPLETED",
    "embedding":[...]
}
