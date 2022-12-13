#!/usr/bin/python3

from db import Book
from app import App

HOST="localhost"
USER="MyUser"
PASSWORD="MainPassword"
DATABASE="Store"

book = Book(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

app = App(book)
app.run(debug=True)