from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Get absolute path to database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "netflix.db")

# -------------------------------
# Get all data
# -------------------------------
def get_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM netflix")
    data = cursor.fetchall()
    conn.close()
    return data

# -------------------------------
# Home page
# -------------------------------
@app.route("/")
def home():
    return """
    <h1>Welcome to Netflix Database</h1>
    <a href='/data'>View Data</a><br><br>
    <a href='/add'>Add New Record</a><br><br>
    <a href='/about'>About</a>
    """

# -------------------------------
# View Data
# -------------------------------
@app.route("/data")
def data():
    data = get_data()
    return render_template("data.html", data=data)

# -------------------------------
# Search
# -------------------------------
@app.route("/search", methods=["POST"])
def search():
    keyword = request.form["keyword"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM netflix WHERE title LIKE ?",
        ('%' + keyword + '%',)
    )

    result = cursor.fetchall()
    conn.close()

    return render_template("data.html", data=result)

# -------------------------------
# Add New Record (NEW FEATURE ⭐)
# -------------------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        type_ = request.form["type"]
        country = request.form["country"]
        year = request.form["year"]
        rating = request.form["rating"]
        duration = request.form["duration"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO netflix (title, type, country, release_year, rating, duration)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, type_, country, year, rating, duration))

        conn.commit()
        conn.close()

        return "<h3>Record Added Successfully!</h3><a href='/data'>Back to Data</a>"

    return render_template("add.html")

# -------------------------------
# About Page
# -------------------------------
@app.route("/about")
def about():
    return render_template("about.html")

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)