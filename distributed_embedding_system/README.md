# Distributed Embedding System (MVP)

## Install

```bash
pip install -r requirements.txt
```

---

## Terminal 1

Run Worker

```bash
python worker.py
```

---

## Terminal 2

Run API

```bash
uvicorn app:app --reload
```

---

## Open

```
http://127.0.0.1:8000/docs
```

---

## Create Job

POST

```
/embeddings
```

Body

```json
{
  "text": "Hello World"
}
```

Response

```json
{
  "job_id":"....",
  "status":"PENDING"
}
```

---

## Check Status

GET

```
/jobs/{job_id}
```

Initially

```json
{
    "status":"PENDING"
}
```

After worker completes

```json
{
    "job_id":"...",
    "status":"COMPLETED",
    "embedding":[...]
}
```