from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import random

app = Flask(__name__)


def load_demo_embeddings():
    raw_data = {
        "káva": [0.95, 0.90, 0.10, 0.05, 0.85],
        "espresso": [0.92, 0.88, 0.12, 0.04, 0.82],
        "kofeín": [0.88, 0.85, 0.15, 0.10, 0.78],
        "čaj": [0.80, 0.85, 0.10, 0.05, 0.70],
        "šálka": [0.75, 0.70, 0.25, 0.05, 0.65],
        "raňajky": [0.65, 0.75, 0.20, 0.15, 0.60],
        "mlieko": [0.60, 0.72, 0.15, 0.10, 0.55],
        "voda": [0.50, 0.65, 0.20, 0.15, 0.40],
        "koláč": [0.45, 0.60, 0.25, 0.20, 0.45],
        "stôl": [0.30, 0.35, 0.60, 0.25, 0.20],
        "kuchyňa": [0.35, 0.40, 0.55, 0.20, 0.30],
        "auto": [0.10, 0.05, 0.80, 0.90, 0.10],
        "vlak": [0.08, 0.05, 0.85, 0.88, 0.08],
        "počítač": [0.15, 0.10, 0.75, 0.70, 0.25],
        "pes": [0.12, 0.20, 0.30, 0.40, 0.15],
        "mačka": [0.14, 0.22, 0.28, 0.38, 0.16],
        "les": [0.05, 0.15, 0.40, 0.20, 0.05],
        "kameň": [0.02, 0.01, 0.90, 0.10, 0.01],
        "bager": [0.01, 0.01, 0.95, 0.95, 0.01],
    }

    words = list(raw_data.keys())
    word2idx = {word: idx for idx, word in enumerate(words)}
    matrix = np.array(list(raw_data.values()), dtype=np.float32)
    return words, word2idx, matrix


WORDS, WORD2IDX, EMBEDDING_MATRIX = load_demo_embeddings()
TOTAL_WORDS = len(WORDS)


def compute_rankings(secret_word):
    target_idx = WORD2IDX[secret_word]
    target_vec = EMBEDDING_MATRIX[target_idx]

    dot_products = EMBEDDING_MATRIX @ target_vec
    norms = np.linalg.norm(EMBEDDING_MATRIX, axis=1) * np.linalg.norm(target_vec)
    similarities = dot_products / (norms + 1e-10)

    sorted_indices = np.argsort(similarities)[::-1]
    rankings = {}
    for rank, idx in enumerate(sorted_indices, start=1):
        word = WORDS[idx]
        rankings[word] = {
            "rank": rank,
            "similarity": float(similarities[idx]),
        }
    return rankings


def pick_new_secret(exclude_word=None):
    candidates = [w for w in WORDS if w != exclude_word]
    return random.choice(candidates if candidates else WORDS)


SECRET_WORD = pick_new_secret()
RANKINGS = compute_rankings(SECRET_WORD)
ROUND_NUMBER = 1


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/guess", methods=["POST"])
def guess():
    global SECRET_WORD, RANKINGS, ROUND_NUMBER

    data = request.get_json()
    word = data.get("word", "").strip().lower()

    if word not in WORD2IDX:
        return jsonify({
            "error": f"Slovo '{word}' nemám v slovníku! Skús napr. čaj, voda, stôl, auto, pes, bager..."
        }), 404

    info = RANKINGS[word]
    rank = info["rank"]
    won = rank == 1

    if TOTAL_WORDS > 1:
        quality = round(((TOTAL_WORDS - rank) / (TOTAL_WORDS - 1)) * 100)
    else:
        quality = 100

    next_round_started = False
    if won:
        # Vyberieme nové tajné slovo a prepočítame maticu podobností pre ďalšie kolo
        SECRET_WORD = pick_new_secret(exclude_word=word)
        RANKINGS = compute_rankings(SECRET_WORD)
        ROUND_NUMBER += 1
        next_round_started = True

    return jsonify({
        "word": word,
        "rank": rank,
        "total": TOTAL_WORDS,
        "quality": quality,
        "similarity": round(info["similarity"], 3),
        "won": won,
        "next_round_started": next_round_started,
        "round": ROUND_NUMBER,
    })


@app.route("/new-game", methods=["POST"])
def new_game():
    global SECRET_WORD, RANKINGS, ROUND_NUMBER
    SECRET_WORD = pick_new_secret(exclude_word=SECRET_WORD)
    RANKINGS = compute_rankings(SECRET_WORD)
    ROUND_NUMBER += 1
    return jsonify({"round": ROUND_NUMBER})


if __name__ == "__main__":
    app.run(debug=True)
