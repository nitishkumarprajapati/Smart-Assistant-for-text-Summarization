from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    # Huggingface limit is 1024 tokens; truncate or chunk for long input
    text = text[:2000]
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
