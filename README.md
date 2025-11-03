# 🧠 AI Agent for PDF Summarization

## Overview
This project is an AI Agent that automatically summarizes PDF documents.  
It extracts text, processes it using a fine-tuned LLM, and produces concise summaries — saving hours of manual reading.



## ✨ Features
- 📄 Extracts text from PDF files
- 🤖 Uses a fine-tuned model for accurate summarization
- 📊 Evaluates summaries with ROUGE metrics
- 🗂️ Includes interaction logs for transparency
- 🌐 Streamlit web interface for uploading and summarizing PDFs


**Set up Instructions**
``bash``

1.Clone the repository
   ``git clone htts://github.com/Meghana512/pdf-summarizer.git``
   ``cd pdf-summarizer``


2.Create and Activate Virtual Environment
   ``python -m venv .venv``
   ``./.venv/scripts/activate``


3.Install Dependencies
   ``pip install -r requirements.txt``


4.Set the current directory as your path
    ``$env:PYTHONPATH = (Get-Location).Path``


5.Run the Streamlit Web Application
    ``streamlit run app/web_app.py``



## 🧩 Architecture
The agent follows a modular design:
- **PDF Extractor** → Extracts and chunks text
- **Summarizer** → Generates summaries using fine-tuned LLM
- **Evaluator** → Computes ROUGE metrics to measure summary quality

---

## 📊 Model Details
The summarization model is fine-tuned from `google/flan-t5-small` using a dataset of academic and general-domain texts.

---

## 🧪 Evaluation
Evaluation Metrics:
- ROUGE-1, ROUGE-2, and ROUGE-L
- Human evaluation (readability, accuracy)


## 👨‍💻 Author
**Meghana Kadari**  
IIT Kanpur — Computer Science & Engineering.
📧 meghanakadari9@gmail.com

