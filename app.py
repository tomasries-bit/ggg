from flask import Flask, request, jsonify, send_from_directory
import numpy as np

app = Flask(__name__)

# --- 1. DÁTOVÉ ŠTRUKTÚRY Z ÚLOH 1.1 – 1.4 ---
# V reálnom projekte tu načítaš fastText (.vec) alebo GloVe súbor
def load_demo_embeddings():
    # Vytvoríme malý sémantický vesmír pre ukážku (5-rozmerné vektory pre prehľadnosť)
    # Tajné slovo bude "káva"
    raw_data = {
        "káva":        [0.95, 0.90, 0.10, 0.05, 0.85], # CIEĽ (#1)
        "espresso":    [0.92, 0.88, 0.12, 0.04, 0.82],
        "kofeín":      [0.88, 0.85, 0.15, 0.10, 0.78],
        "čaj":         [0.80, 0.85, 0.10, 0.05, 0.70],
        "šálka":       [0.75, 0.70, 0.25, 0.05, 0.65],
        "raňajky":     [0.65, 0.75, 0.20, 0.15, 0.60],
        "mlieko":      [0.60, 0.72, 0.15, 0.10, 0.55],
        "voda":        [0.50, 0.65, 0.20, 0.15, 0.40],
        "koláč":       [0.45, 0.60, 0.25, 0.20, 0.45],
        "stôl":        [0.30, 0.35, 0.60, 0.25, 0.20],
        "kuchyňa":     [0.35, 0.40, 0.55, 0.20, 0.30],
        "auto":        [0.10, 0.05, 0.80, 0.90, 0.10],
        "vlak":        [0.08, 0.05, 0.85, 0.88, 0.08],
        "počítač":     [0.15, 0.10, 0.75, 0.70, 0.25],
        "pes":         [0.12, 0.20, 0.30, 0.40, 0.15],
        "mačka":       [0.14, 0.22, 0.28, 0.38, 0.16],
        "les":         [0.05, 0.15, 0.40, 0.20, 0.05],
        "kameň":       [0.02, 0.01, 0.90, 0.10, 0.01],
        "bager":       [0.01, 0.01, 0.95, 0.95, 0.01], # NAJĎALEJ
    }

    words = list(raw_data.keys())
    # Hash Map: slovo -> index v O(1) čase
    word2idx = {word: idx for idx, word in enumerate(words)}
    # 2D Matica embeddingov (V x D)
    matrix = np.array(list(raw_data.values()), dtype=np.float32)

    return words, word2idx, matrix

WORDS, WORD2IDX, EMBEDDING_MATRIX = load_demo_embeddings()
SECRET_WORD = "káva"

# --- 2. VEKTORIZOVANÁ KOSÍNUSOVÁ PODOBNOSŤ (ÚLOHA 1.4) ---
def compute_rankings(secret_word):
    target_idx = WORD2IDX[secret_word]
    target_vec = EMBEDDING_MATRIX[target_idx]

    # Skalárny súčin cieľového vektora so všetkými riadkami matice naraz
    dot_products = EMBEDDING_MATRIX @ target_vec

    # Dĺžky (normy) vektorov
    norms = np.linalg.norm(EMBEDDING_MATRIX, axis=1) * np.linalg.norm(target_vec)
    similarities = dot_products / (norms + 1e-10)

    # Zoradenie indexov od najpodobnejšieho po najmenej podobné
    sorted_indices = np.argsort(similarities)[::-1]

    # Vytvorenie rebríčka: slovo -> poradie (od 1 po N)
    rankings = {}
    for rank, idx in enumerate(sorted_indices, start=1):
        word = WORDS[idx]
        rankings[word] = {
            "rank": rank,
            "similarity": float(similarities[idx])
        }
    return rankings

RANKINGS = compute_rankings(SECRET_WORD)
TOTAL_WORDS = len(WORDS)

# --- 3. API ENDPOINTY ---
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    word = data.get("word", "").strip().lower()

    if word not in WORD2IDX:
        return jsonify({
            "error": f"Slovo '{word}' nemám v slovníku! Skús napr.: espresso, čaj, voda, stôl, auto, pes, bager..."
        }), 404

    info = RANKINGS[word]
    rank = info["rank"]
    
    # Prepočet poradia na skóre 0 až 10000 (10000 = 1. miesto, 0 = posledné miesto)
    if TOTAL_WORDS > 1:
        score = round(((TOTAL_WORDS - rank) / (TOTAL_WORDS - 1)) * 10000)
    else:
        score = 10000

    return jsonify({
        "word": word,
        "rank": rank,
        "total": TOTAL_WORDS,
        "score": score,
        "similarity": round(info["similarity"], 3),
        "won": (rank == 1)
    })

if __name__ == "__main__":
    print(f"Server beží! Tajné slovo je nastavené. Otvor http://127.0.0.1:5000")
    app.run(debug=True)
