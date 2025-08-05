# 🧠 Project Combo — AI-Powered Text Summarization & Analysis Tool

**Project Combo** is a powerful web-based tool that performs extractive and abstractive summarization using state-of-the-art Natural Language Processing (NLP) techniques. It integrates traditional NLP pipelines via **spaCy** with cutting-edge **pretrained transformer models from Hugging Face**, offering a robust foundation for analyzing and summarizing large volumes of natural language text.

---

## 🔍 Features
- ✂️ **Extractive Summarization** using `spaCy` (sentence scoring and selection)
- 🧠 **Abstractive Summarization** using Hugging Face transformers (e.g., BART, T5)
- 🧪 Clean Flask-based backend for API and UI interaction
- ⚙️ Modular structure for extending to other NLP tasks (e.g., sentiment analysis)
- 🧼 Simple UI for entering and processing text (optional HTML frontend)

---

## 🤖 Pretrained Model Integration
- Uses **Hugging Face Transformers** (via `transformers` library)
- Supports powerful models such as:
  - `facebook/bart-large-cnn` for summarization
  - `t5-small` or `t5-base` for lightweight abstractive summaries
- These models are loaded and run locally or can be hosted via Hugging Face Hub

---

## 🛠 Tech Stack
- **Frontend**: HTML, CSS *(optional)*
- **Backend**: Python, Flask
- **NLP**:
  - `spaCy` for syntactic analysis and extractive summarization
  - `transformers` from Hugging Face for abstractive summaries
- **Environment**: `venv` for virtual environments

---

## 📁 Project Structure
```
project_combo/
│
├── app.py                  # Main Flask app
├── summarization/
│   ├── extractive.py       # Summarization logic with spaCy
│   └── huggingface_abstractive.py  # Hugging Face summarizer
├── templates/
│   └── index.html          # (Optional UI)
├── static/                 # (CSS/JS if any)
├── venv/                   # Python virtual environment
├── requirements.txt        # Dependencies
└── README.md               # Project overview
```

---

## 🚀 How It Works
1. **User submits text** through the UI or terminal.
2. For **extractive summarization**, `spaCy` ranks sentences based on token importance.
3. For **abstractive summarization**, the text is passed to a pretrained Hugging Face model like `bart-large-cnn` or `t5-small`.
4. The result is returned in summarized form.

---

## ✅ Use Cases
- Summarizing research papers or news articles
- Processing customer reviews, meeting transcripts
- Teaching and demonstrating NLP workflows