Create a folder

Create Virtual Environment by following these steps
1. python -m venv venv
2. venv\scripts\activate
3. pip install -qU langchain-core
4. pip install -qU langchain-cohere
5. pip install -qU "langchain[google-genai]"
6. %pip install --quiet --upgrade langchain-text-splitters langchain-community langgraph
7. %pip install -qU pypdf
8. change the file_path (pdf_location) in the llm.py
9. After these changes , create a .env file in the same folder and  add GOOGLE_API_KEY='add your gemini api key here' , COHERE_API_KEY='ADD COHERE API KEY HERE'
10. run this command , python llm.py

FOR COHERE_API REFER : https://dashboard.cohere.com/api-keys
FOR GEMINI_API REFER : https://aistudio.google.com/apikey
