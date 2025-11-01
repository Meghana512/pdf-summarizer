from pdf_extractor import extract_text_from_pdf
from summarizer import SummarizerAgent
from evaluator import evaluate_summary
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="summary.txt")
    args = parser.parse_args()

    text = extract_text_from_pdf(args.input)

    agent = SummarizerAgent(model_path="models/fine_tuned_model")
    summary = agent.summarize(text)

    with open(args.output, "w") as f:
        f.write(summary)

    evaluate_summary(text, summary)
    print("✅ Summary generated and saved.")
