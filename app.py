import streamlit as st
from modules.loader import load_document
from modules.summarizer import generate_summary
from modules.qa_engine import answer_question, generate_challenge_questions
from modules.utils import extract_justification

st.set_page_config(page_title="GenAI Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    doc_text = load_document(uploaded_file)
    st.subheader("🔍 Auto Summary")
    st.write(generate_summary(doc_text))

    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask your question here")
        if question:
            answer, score = answer_question(question, doc_text)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"**Confidence:** {score:.2f}")
            st.markdown(f"**Justification:** {extract_justification(answer, doc_text)}")

    elif mode == "Challenge Me":
        st.subheader("🤖 Try answering these:")
        questions = generate_challenge_questions(doc_text)
        for idx, (q, answer_ref) in enumerate(questions):
            user_ans = st.text_input(f"Q{idx+1}: {q}")
            if user_ans:
                match = "✅ Correct!" if user_ans.lower() in answer_ref.lower() else "❌ Not quite"
                st.markdown(f"**Your Answer:** {user_ans}")
                st.markdown(f"**Expected Context:** {answer_ref}")
                st.markdown(f"**Feedback:** {match}")
