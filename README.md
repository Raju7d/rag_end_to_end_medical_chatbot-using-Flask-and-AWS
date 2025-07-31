# rag_end_to_end_medical_chatbot-using-Flask-and-AWS

# Problem statemet



# steps
1. Create a template.sh file and write the directory over there
2. Copy the Medical book to data folder
3. activate the virtual environment (python -m venv .venv) => .\.venv\Scripts\Activate
4. install the requirements.txt file ==> pip install requirements.txt
5. change the ipynb kernel to virtual environment kernel and start testing the coding in locally in jupyter file
6. Follow the Rag approach
    1. Load the data
    2. chunk it
    3. download the embeddings from huggingface or you can use paid embeddings model
    4. create a pinecone client
    5. create an index within the pinecone (Steps mentioned in trails.ipynb)
    6. store the embeddings in a pinecone vector db
    7. Create openai client and prompt template
    8. create a retriver
    9. retrive the relavant documents from the knowledge base
    10. pass that information to LLM
7. write a modular code in src
8. download or write the html and css code from the gooogle (free chatbot templates)
9. create an api's integrate them in a app.py
10. Run the app.py so that you can see the output in  localhost:8080 port

## Steps to follow deploy the application in AWS

