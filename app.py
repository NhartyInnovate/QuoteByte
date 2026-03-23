import csv
import os
import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__, static_folder="public", static_url_path="/public")
app.secret_key = "daily-quotes-secret-key"

QUOTES_FILE = "quotes.csv"
SUBSCRIBERS_FILE = "subscribers.csv"


def get_random_quote():
    if not os.path.exists(QUOTES_FILE):
        return {
            "Quote": "Stay consistent. Small efforts repeated daily create great results.",
            "Author": "Unknown",
            "Tags": "motivation, consistency"
        }

    with open(QUOTES_FILE, newline="", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))
        if not reader:
            return {
                "Quote": "Stay consistent. Small efforts repeated daily create great results.",
                "Author": "Unknown",
                "Tags": "motivation, consistency"
            }
        return random.choice(reader)


def save_email(email):
    file_exists = os.path.exists(SUBSCRIBERS_FILE)

    if file_exists:
        with open(SUBSCRIBERS_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Email"].strip().lower() == email.strip().lower():
                    return False

    with open(SUBSCRIBERS_FILE, "a", newline="", encoding="utf-8") as file:
        fieldnames = ["Email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({"Email": email})

    return True


@app.route("/", methods=["GET", "POST"])
def home():
    quote = get_random_quote()

    if request.method == "POST":
        email = request.form.get("email", "").strip()

        if not email:
            flash("Please enter your email address.")
            return redirect(url_for("home"))

        if "@" not in email or "." not in email:
            flash("Please enter a valid email address.")
            return redirect(url_for("home"))

        saved = save_email(email)

        if not saved:
            flash("This email is already subscribed.")
            return redirect(url_for("home"))

        flash("You have successfully subscribed for daily quotes.")
        return redirect(url_for("home"))

    return render_template("index.html", quote=quote)

@app.route("/random-quote")
def random_quote():
    quote = get_random_quote()
    return jsonify(quote)

if __name__ == "__main__":
    app.run()