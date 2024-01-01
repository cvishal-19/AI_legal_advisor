# AI Legal Advisor README

## Architecture:

![image](https://github.com/cvishal-19/AI_legal_advisor/assets/142085676/a44ef0de-9b02-48d4-8f99-054b634b9ed1)


## Overview:
1. **Document Loading:**
   - Legal documents, including the Constitution of India, IPC acts, and case examples, are loaded for analysis.

2. **Text Preprocessing:**
   - Documents are processed to extract meaningful chunks for further analysis.

3. **Embeddings using Hugging Face:**
   - Utilizing Hugging Face's `sentence-transformers` library for generating embeddings, specifically the `sentence-transformers/all-MiniLM-L6-v2` model.

4. **Vector Storage with CHROMAdb:**
   - Efficient vector storage with CHROMAdb, ensuring optimized retrieval of vectorized legal document chunks.

5. **Similarity Search with Cosine Similarity:**
  - Cosine similarity is employed to measure the similarity between vectorized chunks, enhancing the accuracy of information retrieval.

6. **Chat Model using OpenAI's GPT-3.5-turbo:**
   - Integration of OpenAI's `GPT-3.5-turbo` for natural language interaction.

7. **Deployment with Streamlit:**
   - The system is deployed using Streamlit, providing a user-friendly interface.

## App screenshot
![huh](https://github.com/cvishal-19/AI_legal_advisor/assets/142085676/4d2e3149-86d7-4eb4-9c9e-ec8e4edc1d6d)

## Direction of Use
1. Git clone the Repo in your pc.
2. Install the prerequisites. {`streamlit`, `chromadb`, `openai`, `langchain`, `pypdf`, `sentence-transformers`}
3. Change the openAI API key to your own API key, that one that I have used here, is already `expired`.
4. You will also need to correct the file location for the documents in `deploy_app.py` and  `app.py`.
5. If you want to experiment in your Python shell itself, run `app.py`.
6. And if you want the interface, execute `streamlit run deploy_app.py`.
7. If all above shows a dependency error, you might want to shift to `google Colab`.
8. Upload all the repo in your drive, repeat step 3 and 4, run all the cells in  `run_streamlit_on_colab.ipynb`

Kudos :)
   
