from pymongo import MongoClient
from mongo_db_config import USER, PASSWORD

url = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.gczudfy.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a MongoClient instance
client = MongoClient(url)

# Create collections
db = client.Books
books_fantasy_coll = db.Fantasy_books
books_school_coll = db.School_books

# Adding objects to collections
books_fantasy_coll.insert_one(
    {
        'title': 'Game of thrones',
        'price': 650,
        'year': 2012,
        'pages': 653,
    }
)

school_books = [
    {'title': 'History', 'class': 7, 'pages': 54, 'year': 2020},
    {'title': 'Math', 'class': 3, 'pages': 52, 'year': 2023},
    {'title': 'English', 'class': 10, 'pages': 127, 'year': 2019},
    {'title': 'Biology', 'class': 8, 'pages': 31, 'year': 2022},
    {'title': 'Geography', 'class': 9, 'pages': 56, 'year': 2007},
    ]

books_school_coll.insert_many(school_books)

# Retrieve object
result = books_school_coll.find_one({'title': 'History'})
print(result)

# Updating collections
current_filter = {'title': 'Game of thrones'}
print(books_fantasy_coll.find_one(current_filter))
new_data = {'$inc': {'price': 56}}
book_result = books_fantasy_coll.update_one(current_filter, new_data)
print(books_fantasy_coll.find_one(current_filter))

# Deleting objects
query = {'title': 'Game of thrones'}
data = books_fantasy_coll.delete_one(query)
print(data.raw_result)

query1 = {'year': {'$lt': 2020}}
data1 = books_school_coll.delete_many(query1)
print(data1.raw_result)

