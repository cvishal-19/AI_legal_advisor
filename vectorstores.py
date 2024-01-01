from langchain.vectorstores import Chroma

class VectorStoreCreator:
    def __init__(self, documents, embedding):
        self.documents = documents
        self.embedding = embedding

    def create_vector_store(self):
        return Chroma.from_documents(documents=self.documents, embedding=self.embedding)
