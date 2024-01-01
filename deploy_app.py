import streamlit as st
import time
import getpass
import os
from document_loaders import DocumentLoader
from embeddings import EmbeddingsHandler
from vectorstores import VectorStoreCreator
from chat_model import ChatModel
from langchain.vectorstores import Chroma
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough



file_paths = [
    "V:\Lets try something new\hmm\doc\constituion of india.pdf",
    "V:\Lets try something new\hmm\doc\criminal law.pdf",
    "V:/Lets try something new/hmm/doc/family_law.pdf",
    "V:\Lets try something new\hmm\doc\ipc_act.pdf"
]

document_loader = DocumentLoader(file_paths)
docsi = document_loader.load_and_split_documents()
docsi = [doc for doc_list in docsi for doc in doc_list]

embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings_handler = EmbeddingsHandler(model_name=embedding_model_name)
embedding = embeddings_handler.setup_embeddings()

vectorstore_creator = VectorStoreCreator(documents=docsi, embedding=embedding)
vectorstore = vectorstore_creator.create_vector_store()

vectorstore = Chroma.from_documents(documents=docsi, embedding=embedding)
retriever = vectorstore.as_retriever(search_type = "similarity", search_kwargs = {"k":3})

os.environ['OPENAI_API_KEY'] = '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'
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = getpass.getpass()

llm = ChatModel(model_name='gpt-3.5-turbo', temperature=0.7)

template = """Use the following pieces of context to analyze the case at the end.
See, you are the legal advisor, you specialize in the constitution of India, the ipc acts, the criminal laws and the family laws.
Given the case you are supposed to give the supporting articles from constitution, and supporting IPC acts, and supporting strong advice.
Do not hallucinate.
Be confident.
Be Precise, funny, creative, intelligent, rude at the same time.
always give the supporting numbers.
add some high-fi university abuses too.
{context}
Case: {question}
Answer: ?"""
    
from langchain.prompts import PromptTemplate
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_prompt_custom = PromptTemplate.from_template(template)
rag_chain = (
    {"context":retriever | format_docs, "question" : RunnablePassthrough()}
    | rag_prompt_custom
    | llm
    | StrOutputParser()
)
def handle_chat():
    chathistory = []
    summary_prompt = 'summarize all the points stated, do not leave any details:    '
    chathistory.append(summary_prompt)

    while True:
        msg = st.text_input("Enter your message:")
        if msg:
            time.sleep(10)
            if len(chathistory) == 1:
                output = (rag_chain.invoke((msg)))
                chathistory.append(msg)
                st.write(output)
            else:
                all_previous_messeges_with_prompt = ' '.join(chathistory)
                summary = str(llm.invoke((all_previous_messeges_with_prompt)))
                main_summary_prompt = 'Here is summary of the previous chat, keep can might want to use that for reference: '
                final_chat_summary = main_summary_prompt + summary
                to_ask = final_chat_summary + "\n" + " and the further case is: " + msg
                
                output = (rag_chain.invoke((to_ask)))
                chathistory.append(msg)    
                st.write(output)

def main():
    st.title("Chat App")
    if st.button("New Chat"):
        handle_chat()

if __name__ == "__main__":
    main()
