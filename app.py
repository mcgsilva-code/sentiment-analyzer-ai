from transformers import pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)
print("===ANALISADOR DE SENTIMENTOS ===")
texto = input("Digite um texto para analisar: ")
resultado = classifier(texto)[0]
label = resultado['label']
score = round(resultado['score'], 3)

print(f"\nSentimento: {label}")
print(f"Confiança: {score}")
