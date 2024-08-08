import json

class Book:
    def __init__(self,name,year,author,id):
        self.id = id
        self.name =name
        self.year = year
        self.author = author

class Library:
    def __init__(self):
        self.database = json.load(open('./database.json'))
    
    def Add_book(self):
        pass

    def remove_book(self):
        pass

    def search_book(self):
        pass

    def get_all_books(self):
        pass

library = Library()
#print(library.database['book1']) 