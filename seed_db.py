# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS scores (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     player_name TEXT NOT NULL,
#     score INTEGER NOT NULL,
#     date TEXT
# )
# """)

# cursor.execute("DELETE FROM scores")

# sample_scores = [
#     ("Alice", 120, "2026-03-01"),
#     ("Bob", 98, "2026-03-02"),
#     ("Charlie", 85, "2026-03-03"),
#     ("Dana", 76, "2026-03-04"),
#     ("Evan", 60, "2026-03-05"),
# ]

# cursor.executemany(
#     "INSERT INTO scores (player_name, score, date) VALUES (?, ?, ?)",
#     sample_scores
# )

# conn.commit()
# conn.close()

# print("Database seeded successfully!")


from db import get_db

db = get_db()

cursor = db.cursor()

cursor.execute("DELETE FROM scores")

cursor.execute("INSERT INTO scores (player_name, score, date) VALUES ('Alice',120,'2026-03-01')")
cursor.execute("INSERT INTO scores (player_name, score, date) VALUES ('Bob',95,'2026-03-02')")
cursor.execute("INSERT INTO scores (player_name, score, date) VALUES ('Charlie',80,'2026-03-03')")

db.commit()