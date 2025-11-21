# MULTILINGUAL SENTIMENT ANALYZER

This project uses a **multilingual BERT model** to analyze the sentiment of text inputs in multiple languages.  
It classifies text from **negative to positive** and provides a **confidence score** for each prediction.

---

## TECHNOLOGIES USED

- Python 3.x  
- Hugging Face Transformers  
- PyTorch  
- Model: `nlptown/bert-base-multilingual-uncased-sentiment`

---

## HOW TO RUN

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/multilingual-sentiment-analyzer.git
Install dependencies:

bash
Copia codice
pip install transformers torch
Run the program:

bash
Copia codice
python sentiment_analyzer.py
Enter a text when prompted to see the sentiment and confidence score.

EXAMPLE USAGE
vbnet
Copia codice
=== SENTIMENT ANALYZER ===
Enter a text to analyze: I love programming!
Sentiment: 5 stars
Confidence: 0.987
HOW IT WORKS

The code uses Hugging Face's pipeline function with a pre-trained multilingual BERT model.

For each input text, it returns:

label → sentiment (from "1 star" to "5 stars")

score → model confidence in the prediction

POSSIBLE IMPROVEMENTS / FUTURE IDEAS

Add a simple GUI using Tkinter or Streamlit

Allow analyzing multiple texts at once

Translate the output automatically to English or other languages

Compare results between different BERT models
