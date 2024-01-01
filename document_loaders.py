from langchain.document_loaders import PyPDFLoader

class DocumentLoader:
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def load_and_split_documents(self):
        loaders = [PyPDFLoader(file_path) for file_path in self.file_paths]
        return [loader.load_and_split() for loader in loaders]
