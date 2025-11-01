from rouge import Rouge

def evaluate_summary(reference_text, generated_summary):
    rouge = Rouge()
    scores = rouge.get_scores(generated_summary, reference_text)
    print("ROUGE Scores:", scores)
    return scores
