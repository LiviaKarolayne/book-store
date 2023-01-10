#!/usr/bin/python3

import mysql.connector

class Book:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def read_all(self):
        books = list()
        sql = "SELECT * FROM books"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        for book in data:
            books.append(
                {
                    "id": book[0],
                    "title": book[1],
                    "author": book[2]
                }
            )
        return books

    def read(self, id):
        book = dict()
        sql = f"SELECT * FROM books WHERE id={id}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        book["id"] = data[0][0]
        book["title"] = data[0][1]
        book["author"] = data[0][2]

        return book 

    def create(self, tilte, author):
        sql = f"INSERT INTO books (title, author) VALUES ('{tilte}', '{author}')"
        self.cursor.execute(sql)
        self.connection.commit()

    def delete(self, id):
        sql = f"DELETE FROM books WHERE id={id}"
        self.cursor.execute(sql)
        self.connection.commit()

    def update(self, id, new_tilte, new_author):
        sql = f"UPDATE books SET title='{new_tilte}', author='{new_author}' WHERE id={id}"
        self.cursor.execute(sql)
        self.connection.commit()

#book = Book(host="localhost", user="MyUser", password="MainPassword", database="Store")
#book.create("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin")
#book.create("Clean Architecture: A Craftsmans Guide to Software Structure and Design", "Robert C. Martin")
#book.create("Design Patterns: Elements Of Reusable Object-oriented Software - Importado - Ingles", "Erich Gamma")
#book.create("Computer Networking: A Top-Down Approach", "James Kurose")
#book.create("title", "author")
#book.delete(id=1)
#book.update("14", "title2", "author2")
#books = book.read_all()
#book = book.read(id=1)
#print(book)
#print(books)


"""
connection = mysql.connector.connect(
    host="localhost",
    user="MyUser",
    password="MainPassword",
    database="Store"
)

cursor_db = connection.cursor()
cursor_db.execute("SELECT * FROM books")
books = cursor_db.fetchall()
print(books)
"""