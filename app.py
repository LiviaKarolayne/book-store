#!/usr/bin/python3

from flask import Flask, request, render_template, redirect, url_for

class App:
    def __init__(self, db):
        self.app = Flask(__name__, template_folder="View", static_folder="View/assets")
        self.db = db
        
        @self.app.errorhandler(404) 
        def not_found(e): 
            return "400 Page not found"

        @self.app.route("/")
        @self.app.route("/index")
        def index():
            return render_template("index.html")

        @self.app.route("/list_books")
        def list_books():
            books = self.db.read_all()
            return render_template("book/list.html", books=books)

        @self.app.route("/form_book", methods=["POST"])
        def form_book():
            request_type = request.form.get("request_type")
            book = {"id":"", "title":"", "author":""}

            if request_type == "Edit":
                id = request.form.get("id")
                book = self.db.read(id)

            return render_template("book/form.html", request_type=request_type, book=book)

        @self.app.route("/set_book", methods=["POST"])
        def set_book():
            request_type = request.form.get("request_type")
            title = request.form.get("title")
            author = request.form.get("author")

            if request_type == "Edit":
                id = request.form.get("id")
                self.db.update(id, title, author)
            else:
                self.db.create(title, author)

            return redirect(url_for("list_books"))

        @self.app.route("/delete_book", methods=["POST"])
        def delete_book():
            id = request.form.get("id")
            self.db.delete(id)
            return redirect(url_for("list_books"))

    def run(self, *args, **kwargs):
        return self.app.run(*args, **kwargs)