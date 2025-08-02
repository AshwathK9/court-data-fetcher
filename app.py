from flask import Flask, render_template, request
from scraper import fetch_case_data
import sqlite3
from datetime import datetime

app = Flask(__name__)

def log_to_db(case_type, case_number, year, html, parsed):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("INSERT INTO queries (case_type, case_number, year, html, parsed_json, created_at) VALUES (?, ?, ?, ?, ?, ?)", 
              (case_type, case_number, year, html, str(parsed), datetime.now()))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    year = request.form["year"]

    try:
        raw_html, parsed = fetch_case_data(case_type, case_number, year)
        log_to_db(case_type, case_number, year, raw_html, parsed)
        return render_template("index.html", result=parsed)
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
