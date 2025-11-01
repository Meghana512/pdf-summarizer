from transformers import pipeline

class SummarizerAgent:
    def __init__(self, model_path="google/flan-t5-small"):
        self.summarizer = pipeline("summarization", model=model_path)

    def summarize(self, text, max_length=300, min_length=100):
        chunks = [text[i:i+2000] for i in range(0, len(text), 2000)]
        summaries = []
        for chunk in chunks:
            summaries.append(self.summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text'])
        return " ".join(summaries)
