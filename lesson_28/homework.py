import sqlite3

with sqlite3.connect('books_authors.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    query = """
         CREATE TABLE IF NOT EXISTS authors_library(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            country VARCHAR(30) NOT NULL
            )"""
    cursor.execute(query)

    query = """
         CREATE TABLE IF NOT EXISTS books_library(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title VARCHAR(50) NOT NULL,
            price DECIMAL(8, 2) NOT NULL CHECK (price > 0),
            pages_quantity INTEGER NOT NULL CHECK (pages_quantity > 0),
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors_library(id)
            )"""
    cursor.execute(query)

    # ADD MANY AUTHORS
    # values = [
    #     ('Іан', 'Вайброу', 'Норвегія'),
    #     ('Джейсон', 'Бріггс', 'Ірландія'),
    #     ('Ерін', 'Гантер', 'Австралія'),
    #     ('Павел', 'Виктор', 'Україна'),
    #     ('Девід', 'Вольямс', 'США')
    # ]
    #
    # query = """
    #     INSERT INTO authors_library(name, last_name, country)
    #     VALUES (?, ?, ?)
    # """
    #
    # cursor.executemany(query, values)
    #
    # ADD MANY BOOKS
    # values = [
    #     ('Малий Вовчик', 290, 142, 1),
    #     ('Шлях Вогнезора', 590, 522, 3),
    #     ('Python для дітей', 350, 360, 2),
    #     ('Погані діти', 269, 259, 5),
    #     ('Scratch для дітей', 289, 312, None)
    # ]
    #
    # query = """
    #     INSERT INTO books_library(title, price, pages_quantity, author_id)
    #     VALUES (?, ?, ?, ?)
    # """
    #
    # cursor.executemany(query, values)

    # SELECT INNER JOIN
    # query = """
    #     SELECT books_library.title, books_library.price, authors_library.name, authors_library.last_name
    #     FROM books_library
    #     INNER JOIN authors_library ON authors_library.id = books_library.author_id
    # """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep=';\n')
    #
    # SELECT LEFT JOIN
    # query = """
    #     SELECT books_library.title, books_library.price, authors_library.name, authors_library.last_name
    #     FROM books_library
    #     LEFT JOIN authors_library ON authors_library.id = books_library.author_id
    # """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep=';\n')

    # query = """
    #         SELECT books_library.title, books_library.price, authors_library.name, authors_library.last_name
    #         FROM books_library
    #         FULL JOIN authors_library ON authors_library.id = books_library.author_id
    #     """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep=';\n')
