import sqlite3

with sqlite3.connect('books_db.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS books_library(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name VARCHAR(50) NOT NULL,
    #         pages_quantity INTEGER NOT NULL CHECK (pages_quantity > 0),
    #         price DECIMAL(8, 2) NOT NULL CHECK (price > 0)
    #         )
    # """
    # cursor.execute(query)
    #
    # ADD ONE BOOK
    # name = 'Python для дітей'
    # pages_quantity = 389
    # price = 100
    #
    # values = [name, price, pages_quantity]
    #
    # ADD MANY BOOKS
    # query = """
    #     INSERT INTO books_library(name, price, pages_quantity)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)
    #
    # values = [
    #         ('Історія України', 340, 100),
    #         ('Математика', 100, 670),
    #         ('Фізика', 45, 370),
    #         ('Ляльководи', 230, 73.55),
    #         ('Зоряні війни', 590, 1100.50),
    #         ('Історія чогось', 70, 550.75),
    #         ('Всесвітня історія', 290, 485)
    #     ]
    #
    # query = """
    #     INSERT INTO books_library(name, pages_quantity, price)
    #     VALUES (?, ?, ?)
    # """
    #
    # cursor.executemany(query, values)
    #
    # READ BOOKS THAT ARE M0RE THAN PRiCE 100
    # query = """
    #     SELECT name, price
    #     FROM books_library
    #     WHERE price > 100
    # """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep='\n')
    #
    # READ CHEAPEST BOOKS
    # query = """
    #     SELECT name, price
    #     FROM books_library
    #     ORDER BY price ASC
    #     LIMIT 3
    # """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep='\n')
    #
    # READ HISTORY BOOKS
    # query = """
    #     SELECT name, price
    #     FROM books_library
    #     WHERE name LIKE '%Історія%' or name LIKE '%історія%'
    #     LIMIT 2
    # """
    # result = cursor.execute(query)
    # print(*result.fetchall(), sep='\n')
    #
    # UPDATE
    # query = """
    #     ALTER TABLE books_library
    #     ADD COLUMN digit_code DEFAULT '0-00000'
    # """
    # cursor.execute(query)
    #
    # query = """
    #     UPDATE books_library
    #     SET digit_code = id || '-12435'
    #     WHERE pages_quantity > 200
    # """
    # cursor.execute(query)
    #
    # DELETE
    # query = """
    #     DELETE FROM books_library
    #     WHERE price = 100
    # """
    # cursor.execute(query)
