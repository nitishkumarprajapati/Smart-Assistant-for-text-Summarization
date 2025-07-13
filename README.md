# Smart-Assistant-for-text-Summarization
# 🤖 Smart Assistant for Research Summarization

This project is part of an internship task for EZ. It’s an AI-powered assistant that reads user-uploaded documents (PDF/TXT) and performs deep summarization, question answering, and reasoning-based challenge evaluation — all locally using free and open-source models.

---

## 🚀 Features

- 📄 **Upload PDF or TXT** files
- ✨ **Auto Summary** of the document in ≤ 150 words
- 🧠 **Ask Anything**: Ask any question related to the document, get contextual answers with justification
- 🎯 **Challenge Me**: AI generates logic-based questions, evaluates your answers, and gives feedback
- 📌 Justifies every answer using content from the document
- 🧰 **Streamlit UI**: Clean and interactive local web interface
- 🆓 **No paid APIs**: 100% open-source and offline-compatible

---

## 🧱 Architecture Overview

User → Streamlit UI → Document Loader
↓ ↓
Ask Anything Challenge Me
↓ ↓
Q&A Pipeline Logic QA Gen
↓ ↓
Justification Extractor (utils)

- Uses **Hugging Face Transformers** (`DistilBERT` & `DistilBART`) for local NLP tasks
- Uses `nltk` for sentence tokenization and logic question generation
- Document content is held in memory and all answers are contextually grounded

---

## 📁 Project Structure

genai_assistant/
│
├── app.py # Streamlit main file
├── modules/
│ ├── loader.py # Load PDF/TXT
│ ├── summarizer.py # Document summarization
│ ├── qa_engine.py # Q&A and logic-based challenge mode
│ └── utils.py # Justification extraction
├── requirements.txt
└── README.md # 

##Create a virtual environment
  python -m venv venv
venv\Scripts\activate  # On Windows

##Install dependencies:
pip install -r requirements.txt

##Run the app:
streamlit run app.py

## Model used
| Feature       | Model Name                              | Source       |
| ------------- | --------------------------------------- | ------------ |
| Summarization | `sshleifer/distilbart-cnn-12-6`         | Hugging Face |
| Q\&A          | `distilbert-base-cased-distilled-squad` | Hugging Face |

## Example and usesCases
| Mode         | Example                                                 |
| ------------ | ------------------------------------------------------- |
| Ask Anything | *"What are the key findings in the second section?"*    |
| Challenge Me | *"AI asks: What does 'X' mean? You answer, it scores."* |

## 📄 License
This project is built for educational and internship evaluation purposes under the EZ internship guidelines.

## 🙋‍♂️ Author
Nitish Kumar Prajapati
B.Tech CSE | NIET |https://www.linkedin.com/in/nitish-kumar-prajapati-9937b52a6/

