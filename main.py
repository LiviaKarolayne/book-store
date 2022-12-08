#!/usr/bin/python3

from db import Book
from app import App

book = Book(host="localhost", user="MyUser", password="MainPassword", database="Store")
app = App(book)
app.run(debug=True)