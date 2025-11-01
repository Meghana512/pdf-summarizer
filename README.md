# 🧠 AI Agent for PDF Summarization

## Overview
This project is an AI Agent that automatically summarizes PDF documents.  
It extracts text, processes it using a fine-tuned LLM, and produces concise summaries — saving hours of manual reading.

---

## ✨ Features
- 📄 Extracts text from PDF files
- 🤖 Uses a fine-tuned model for accurate summarization
- 📊 Evaluates summaries with ROUGE metrics
- 🗂️ Includes interaction logs for transparency
- 🌐 Streamlit web interface for uploading and summarizing PDFs

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/<your-username>/pdf-summarizer-ai-agent.git
cd pdf-summarizer-ai-agent

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Command Line
```bash
python src/main.py --input data/sample.pdf --output summary.txt
```

### Web App
```bash
streamlit run app/web_app.py
```

---

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

---

## 📜 Deliverables
- ✅ Source Code (this repo)
- ✅ Architecture Document (`docs/architecture.md`)
- ✅ Data Science Report (`docs/data_science_report.md`)
- ✅ Interaction Logs (`logs/interaction_log.txt`)
- ✅ (Optional) Demo Screenshots

---

## 👨‍💻 Author
**Perugu Rishi Kiran**  
VIT University — Department of Computer Science  
📧 jeshwanthgattam@gmail.com
