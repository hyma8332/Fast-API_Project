from transformers import pipeline

# # Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(
        text,
        max_length=100,
        min_length=30,
        do_sample=False
    )
    return summary[0]["summary_text"]

# def summarize_text(text):
#     words = text.split()

#     if len(words) <= 50:
#         return text

#     return " ".join(words[:50]) + "..."