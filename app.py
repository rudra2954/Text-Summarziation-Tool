from flask import Flask, render_template, request, jsonify
from summarization.extractive import extractive_summary
from summarization.abstractive import abstractive_summary

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the index.html from the templates folder
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get JSON data from the POST request
        data = request.get_json()
        text = data.get("text")  # Input text
        method = data.get("method")  # Summarization method (extractive or abstractive)

        if not text:
            return jsonify({"error": "Text input is required"}), 400  # Error if text is missing

        # Call appropriate summarization method
        if method == 'extractive':
            summary = extractive_summary(text)
        elif method == 'abstractive':
            summary = abstractive_summary(text)
        else:
            return jsonify({"error": "Invalid summarization method"}), 400  # Error if method is invalid

        return jsonify({"summary": summary})  # Return the summary as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return any unexpected errors

if __name__ == '__main__':
    app.run(debug=True)