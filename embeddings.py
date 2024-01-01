from langchain.embeddings.huggingface import HuggingFaceEmbeddings

class EmbeddingsHandler:
    def __init__(self, model_name):
        self.model_name = model_name

    def setup_embeddings(self):
        return HuggingFaceEmbeddings(model_name=self.model_name)