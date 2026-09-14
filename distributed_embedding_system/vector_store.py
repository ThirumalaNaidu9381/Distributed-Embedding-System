class VectorStore:

    def __init__(self):
        self.vectors = {}

    def store(self, job_id, embedding):

        self.vectors[job_id] = embedding

    def get(self, job_id):

        return self.vectors.get(job_id)


vector_store = VectorStore()