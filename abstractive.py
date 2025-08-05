import requests

# Hugging Face API endpoint for BART model
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def abstractive_summary(text, chunk_size=500):
    """
    Function to generate an abstractive summary from input text by chunking and sending to Hugging Face API.
    """
    # Split the text into chunks to avoid exceeding the maximum input size for the API.
    sentences = text.split('.')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    summaries = []
    for chunk in chunks:
        # Request summary for each chunk from Hugging Face API
        response = requests.post(API_URL, headers=headers, json={"inputs": chunk})
        if response.status_code == 200:
            summaries.append(response.json()[0]["summary_text"])
        else:
            summaries.append(f"Error summarizing chunk: {response.status_code}")

    # Combine and return all summarized chunks as a single summary
    return " ".join(summaries)