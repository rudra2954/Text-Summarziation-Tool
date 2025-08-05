import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def extractive_summary(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Rank sentences by their importance (here, we use sentence length as a proxy)
    sentences = [sent.text.strip() for sent in doc.sents]
    sentences.sort(key=lambda x: len(x), reverse=True)  # Sort sentences by length (for simplicity)
    
    # Return top 3 longest sentences as summary (you can adjust this logic)
    return " ".join(sentences[:3])



