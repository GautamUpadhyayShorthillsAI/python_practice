class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {} # {book : user}

    def add_book(self,book_name):
        """Adds a new book to the library's inventory."""
        if book_name not in self.books:
            self.books.append(book_name)
            return f"'{book_name}' has been added to the library."
        return f"'{book_name}' is already in the library."
    
    def issue_book(self,book_name,user_name):
        if book_name in self.books and book_name not in self.borrowed_books:
            self.books.remove(book_name)
            self.borrowed_books[book_name] = user_name
            return f"'{book_name}' has been issued to {user_name}."
        elif book_name in self.borrowed_books:
            return f"'{book_name}' is already borrowed by {self.borrowed_books[book_name]}."
        else:
             return f"'{book_name}' is not available in the library."

    def return_book(self,book_name):
        if book_name in self.borrowed_books:
            user_name = self.borrowed_books.pop(book_name)  # Remove from borrowed_books
            self.books.append(book_name)  # Add the book back to the books list
            return f"'{book_name}' has been returned by {user_name} and added back to the library."
        else:
            return f"'{book_name}' was not borrowed."

    def check_availability(self,book_name):
        if book_name in self.books and book_name not in self.borrowed_books:
            return f"'{book_name}' is available in the library."
        elif book_name in self.borrowed_books:
            return f"'{book_name}' is currently borrowed."
        else:
            return f"'{book_name}' is not available in the library."


lib1 = Library()

add = lib1.add_book("Harry Ptter")
check = lib1.check_availability("Harry Potter")
borr = lib1.issue_book("Harry Potter","Gautam")
print(add)
print(check)
print(borr)
