from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date


# create a flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)


class MyBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    number_of_pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(128), nullable=False, default="-")
    input_date = db.Column(db.String(32), nullable=False, default=date.today)


# basic route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    my_books = MyBook.query.order_by(MyBook.id).all()
    return render_template("books.html", template_books = my_books)


@app.route("/books/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        book_title = request.form["title"]
        book_author = request.form["author"]
        book_content = request.form["content"]
        book_number_of_pages = request.form["number_of_pages"]
        book_isbn = request.form["isbn"]
        new_book = MyBook(
            title=book_title,
            author=book_author,
            content=book_content,
            number_of_pages=book_number_of_pages,
            isbn=book_isbn,
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("books"))
    else:
        return render_template("new_book.html")


@app.route("/books/delete/<int:id>")
def delete(id):
    book = MyBook.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books"))


@app.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = MyBook.query.get_or_404(id)

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.content = request.form["content"]
        book.number_of_pages = request.form["number_of_pages"]
        book.isbn = request.form["isbn"]
        db.session.commit()
        return redirect(url_for("books"))
    else:
        return render_template("edit.html", template_book=book)


# debug mode - it shows us actual errors
if __name__ == "__main__":
    app.run(debug=True)
