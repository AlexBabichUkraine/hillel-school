# import sqlite3
# import hashlib
# from pprint import pprint
#
#
# def encript_password(value: str) -> str:
# @@ -11,6 +12,77 @@ def encript_password(value: str) -> str:
# with sqlite3.connect('new_db.sqlite3') as connection:
#     cursor = connection.cursor()
#     connection.create_function('encode', 1, encript_password)
#     cursor.execute("PRAGMA foreign_keys = ON")

    # values = ['phones', 'samsung']
    # query = """
    #     INSERT INTO category(name, description)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)

    # values = ['M12 v2 2023-1-1', 250, 300, 7]
    # query = """
    #     INSERT INTO device(title, whole_price, price, category_id)
    #     VALUES(?, ?, ?, ?)
    # """
    # cursor.execute(query, values)

    # query = """
    #     SELECT device.title, whole_price, price * 1.2, name, category.description
    # FROM device
    #                  LEFT JOIN category
    #     ON device.category_id = category.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())


# trigger_sql_discount = """
#     CREATE TRIGGER IF NOT EXISTS discount_description_pr
#     AFTER UPDATE ON device
#     WHEN old.price > new.price
#     BEGIN
#         UPDATE device
#         SET description = UPPER('discount') ||  new.price
#         WHERE id=new.id;
#     END;
# """
# cursor.execute(trigger_sql_discount)

# trigger_sql_discount = """
#     CREATE TRIGGER IF NOT EXISTS prem_category
#     AFTER UPDATE ON device
#     WHEN new.price > 5000
#     BEGIN
#         INSERT INTO category (name, description)
#         VALUES ('new premium category', 'top' || new.price);
#     END;
# """
# cursor.execute(trigger_sql_discount)
#
#     trigger_sql_some_new_with_condition = """
#         CREATE TRIGGER IF NOT EXISTS title_validate
#         AFTER UPDATE ON device
#         BEGIN
#             SELECT
#                 CASE
#                     WHEN length(new.title) > 10 THEN
#                         RAISE (ABORT, 'Too long title')
#                     END;
#         END;
#     """
#     cursor.execute(trigger_sql_some_new_with_condition)
#
#     query = """
#         UPDATE device
#         SET
#             title = '0123456789'
#         WHERE
#             id = 10
#     """
#     cursor.execute(query)
#
#
#     # query = """
#     #     CREATE TABLE IF NOT EXISTS user(
# @@ -150,25 +222,25 @@ def encript_password(value: str) -> str:
#     # """
#     # cursor.execute(query)
#
#     query = """
#         UPDATE customers
#         SET
#             balance = 10
#         WHERE
#             balance = 5
#     """
#     # query = """
#     #     UPDATE customers
#     #     SET
#     #         balance = 10
#     #     WHERE
#     #         balance = 5
#     # """
#     # cursor.execute(query)
#
#     print(connection.total_changes)
#     # 1/0
#     query = """
#         UPDATE customers
#         SET
#             balance = 11
#         WHERE
#             balance = 10
#     """
#     # cursor.execute(query)
#     # print(connection.total_changes)
#     # # 1/0
#     # query = """
#     #     UPDATE customers
#     #     SET
#     #         balance = 11
#     #     WHERE
#     #         balance = 10
#     # """
#     # # cursor.execute(query)
#     # DELETE
#     # query = """
#     #     DELETE FROM customers
# @@ -178,39 +250,47 @@ def encript_password(value: str) -> str:

    # cursor.execute(query)
#
#     sqlite_data = 'SELECT sqlite_version()'
#     cursor.execute(sqlite_data)
#     record = cursor.fetchone()
#     print(record)
#     # sqlite_data = 'SELECT sqlite_version()'
#     # cursor.execute(sqlite_data)
#     # record = cursor.fetchone()
#     # print(record)
#     #
#     # print(connection.total_changes)
#
#     print(connection.total_changes)
#     #     CREATE DUMP
#     # with open('dump_db.sql', 'w') as dump:
#     #     for sql in connection.iterdump():
#     #         dump.write(sql)
#     # with open('dump_db.sql', 'r') as dump:
#     #     sql = dump.read()
#     #     cursor.executescript(sql)
#
#
# con2 = sqlite3.connect('new_db.sqlite3')
# try:
#     query = """
#         UPDATE customers
#         SET
#             balance = 15
#         WHERE
#             balance = 10
#     """
#     con2.execute(query)
#
#     print(con2.total_changes)
#     1/0
#     query = """
#         UPDATE customers
#         SET
#             balance = 11
#         WHERE
#             balance = 15
#     """
#     con2.execute(query)
#     con2.commit()
# except:
#     con2.rollback()
#     pass
# finally:
#     con2.close()
# # con2 = sqlite3.connect('new_db.sqlite3')
# # try:
# #     query = """
# #         UPDATE customers
# #         SET
# #             balance = 15
# #         WHERE
# #             balance = 10
# #     """
# #     con2.execute(query)
# #
# #     print(con2.total_changes)
# #     1/0
# #     query = """
# #         UPDATE customers
# #         SET
# #             balance = 11
# #         WHERE
# #             balance = 15
# #     """
# #     con2.execute(query)
# #     con2.commit()
# # except:
# #     con2.rollback()
# #     pass
# # finally:
# #     con2.close()
