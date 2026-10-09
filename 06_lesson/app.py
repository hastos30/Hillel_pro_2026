from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    book_list = [
        "Изучаем Python",
        "Полное руководство по Java",
        "Clean code",
        "Грокаем алгоритмы",
    ]
    return render_template("books.html", books=book_list)


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if not title:
            return render_template("recommend.html", error="Введи название книги.")

        return render_template("recommend.html", title=title)

    return render_template("recommend.html")
