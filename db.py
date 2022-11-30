import mysql.connector

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