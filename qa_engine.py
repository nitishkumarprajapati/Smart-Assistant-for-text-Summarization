from transformers import pipeline
import random
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer'], result['score']

def generate_challenge_questions(context):
    sentences = sent_tokenize(context)
    questions = []
    for _ in range(3):
        sentence = random.choice(sentences)
        q = f"What does this mean: \"{sentence.strip()}\"?"
        questions.append((q, sentence.strip()))
    return questions
