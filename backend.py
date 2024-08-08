import json

class Book:
    def __init__(self,name,year,author,id):
        self.id = id
        self.name =name
        self.year = year
        self.author = author

    def get_key_value(self):
        key_value= {
            "name":self.name,
            "year":self.year,
            "author":self.author
        }
        return key_value

class Library:
    def __init__(self):
        self.database = json.load(open('./database.json'))
    
    def Add_book(self,id,name,year,author):
        if id in self.database.keys():
            raise ValueError
        else:
            newBook= Book(id , name , year , author)
            self.database[id] = newBook.get_key_value()
            try:
                json.dump(
                    self.database,
                    open("./database.json","w"),
                    indent=4 
                )
            except:
                json.dumps()

    def remove_book(self):
        pass

    def search_book(self):
        pass

    def get_all_books(self):
        pass 

library = Library()
library.Add_book(
    "id004",
    "Harry Potter",
    2009,
    "J.K. Rolling"
)
#print(library.database['book1']) 