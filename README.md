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
9. python llm.py
