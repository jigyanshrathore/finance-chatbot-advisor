# finance-chatbot-advisor
📊 Finance Report Summarizer & Q&A Bot
An AI-powered assistant that helps you summarize, analyze, and ask questions about financial reports — directly from a simple and interactive web UI.

Built with Streamlit, LangChain, and OpenAI, this app turns large, complex financial documents into digestible insights for analysts, founders, and researchers.


🚀 Features
📁 Upload: Upload PDF or text-based financial reports

🧠 Summarize: Automatically summarize the entire document

❓ Ask Questions: Get smart, context-aware answers from the document

🧾 Embeddings Search: Uses vector-based retrieval (FAISS) to ground answers in the actual report

🔐 Secure API Key Handling: No secrets exposed in code — uses .env or Streamlit secrets

🛠️ Tech Stack
Tech	Usage
🧠 LangChain	QA Chain & Text Chunking
🦜 OpenAI	GPT-3.5 for summarization & QA
📊 FAISS	Embedding search engine
🖼️ Streamlit	Interactive web frontend
🧬 Tiktoken	Tokenizer for efficient chunking
🔐 Dotenv	Local secret management


▶️ Run Locally
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/finance-chatbot-advisor.git
cd finance-chatbot-advisor
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set up your OpenAI API key
Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
Or add it in Streamlit Secrets if deploying.

4. Run the app
bash
Copy
Edit
streamlit run app.py
☁️ Deploy on Streamlit Cloud
Push this project to a GitHub repo

Go to streamlit.io/cloud

Create a new app from the repo

In the Secrets section of the app, add:

toml
Copy
Edit
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
📌 Sample Use Cases
📈 Annual or quarterly financial report summarization

💬 Interactive data analysis for investors or analysts

📊 Making non-technical stakeholders data-literate

🧾 Automating due diligence review

🧠 How It Works
Text Extraction → From uploaded report

Text Chunking → Using LangChain's splitter

Embeddings Generation → Using OpenAI embeddings

Vector Store Creation → Using FAISS

Summarization → Prompting GPT on full context

QA → LangChain’s RetrievalQA queries top-matching chunks

📃 License
This project is open-source under the MIT License.

🙌 Acknowledgements
OpenAI

LangChain

Streamlit

FAISS by Facebook AI
