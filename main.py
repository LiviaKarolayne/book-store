#!/usr/bin/python3

import sys

from db.db import Book
from app import App

HOST="10.98.208.24"
USER="root"
PASSWORD="RootPassword"
DATABASE="Store"

book = Book(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

app = App(book).run(host="0.0.0.0")