from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser

class ChatModel:
    def __init__(self, model_name, temperature):
        self.model = ChatOpenAI(model_name=model_name, temperature=temperature)
        
