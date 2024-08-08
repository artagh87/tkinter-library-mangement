import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, name, year, author, id):
        self.id = id
        self.name = name
        self.year = year
        self.author = author

    def get_key_value(self):
        key_value = {
            "name": self.name,
            "year": self.year,
            "author": self.author
        }
        return key_value

class Library:
    def __init__(self):
        self.database = self.load_database()

    def load_database(self):
        try:
            with open('./database.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def add_book(self, id, name, year, author):
        if id in self.database.keys():
            raise ValueError("Book ID already exists.")
        else:
            new_book = Book(name, year, author, id)
            self.database[id] = new_book.get_key_value()
            self.save_database()

    def remove_book(self, id):
        if id in self.database:
            del self.database[id]
            self.save_database()
        else:
            raise ValueError("Book ID not found.")

    def search_book(self, id):
        return self.database.get(id, None)

    def save_database(self):
        with open("./database.json", "w") as f:
            json.dump(self.database, f, indent=4)

    def get_all_books(self):
        return self.database

class LibraryApp:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x400")
        self.root.configure(bg="#e0f7fa")  # Light cyan background

        # Title Label
        title_label = tk.Label(root, text="Library Management System", font=("Arial", 16), bg="#e0f7fa", fg="#00796b")
        title_label.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#e0f7fa")
        button_frame.pack(pady=20)

        self.add_book_button = tk.Button(button_frame, text="Add Book", command=self.add_book, width=15, bg="#4caf50", fg="white")
        self.add_book_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_book_button = tk.Button(button_frame, text="Remove Book", command=self.remove_book, width=15, bg="#f44336", fg="white")
        self.remove_book_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_book_button = tk.Button(button_frame, text="Search Book", command=self.search_book, width=15, bg="#2196f3", fg="white")
        self.search_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.view_books_button = tk.Button(button_frame, text="View All Books", command=self.view_books, width=15, bg="#ff9800", fg="white")
        self.view_books_button.grid(row=1, column=1, padx=5, pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", bg="#e0f7fa", fg="#00796b", wraplength=350, justify="left")
        self.result_label.pack(pady=10)

    def add_book(self):
        id = simpledialog.askstring("Input", "Enter Book ID:")
        name = simpledialog.askstring("Input", "Enter Book Name:")
        year = simpledialog.askstring("Input", "Enter Year of Publication:")
        author = simpledialog.askstring("Input", "Enter Author Name:")

        try:
            self.library.add_book(id, name, year, author)
            self.result_label.config(text="Book added successfully!")
        except ValueError as e:
            self.result_label.config(text=str(e))

    def remove_book(self):
        id = simpledialog.askstring("Input", "Enter Book ID to Remove:")
        try:
            self.library.remove_book(id)
            self.result_label.config(text="Book removed successfully!")
        except ValueError as e:
            self.result_label.config(text=str(e))

    def search_book(self):
        id = simpledialog.askstring("Input", "Enter Book ID to Search:")
        book = self.library.search_book(id)
        if book:
            book_info = f"ID: {id}\nName: {book['name']}\nYear: {book['year']}\nAuthor: {book['author']}"
            self.result_label.config(text=book_info)
        else:
            self.result_label.config(text="Book ID not found.")

    def view_books(self):
        books = self.library.get_all_books()
        if not books:
            self.result_label.config(text="No books in the library.")
            return

        book_list = "\n".join([f"ID: {id}, Name: {info['name']}, Year: {info['year']}, Author: {info['author']}" for id, info in books.items()])
        self.result_label.config(text=book_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
