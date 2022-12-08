#!/usr/bin/python3

from flask import Flask, render_template

class App:
    def __init__(self):
        self.app = Flask(__name__, template_folder="View", static_folder="View/assets")
        
        @self.app.errorhandler(404) 
        def not_found(e): 
            return self.send_response("400", "Page not found", "", "")

        @self.app.route("/")
        @self.app.route("/index")
        def index():
            return render_template("index.html")

        @self.app.route("/list_books")
        def list_books():
            books = db.read_all()
            return render_template("list_books.html", books=books)

    def run(self, *args, **kwargs):
        return self.app.run(*args, **kwargs)