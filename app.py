# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Strategy Game API is running!"

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/game")
# def game():
#     return render_template("game.html")

# @app.route("/leaderboard")
# def leaderboard():
#     return render_template("leaderboard.html")

# if __name__ == "__main__":
#     app.run(debug=True)



    
from flask import Flask, jsonify, render_template
from db import get_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/leaderboard-page")
def leaderboard_page():
    return render_template("leaderboard.html")

@app.route("/leaderboard")
def leaderboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT player_name, score, date
        FROM scores
        ORDER BY score DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    results = []
    for row in rows:
        results.append({
            "player": row["player_name"],
            "score": row["score"],
            "date": row["date"]
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)    