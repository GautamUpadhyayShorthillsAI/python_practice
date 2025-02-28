total_books_in_library = 1000;

# Closure to track borrowed books
def create_borrow_counter():
    borrow_count = 0

    def increment_borrow_count():
        nonlocal borrow_count
        borrow_count += 1
        print(f"Books borrowed so far: {borrow_count}")
    
    return increment_borrow_count

class libraryUser:
    total_user = 0
    # Initialize the class with name and book borrowed
    def __init__(self,name):
        self.name = name
        self.books_borrowed = 0 # Increment when book borrowed
        libraryUser.total_user += 1 #increment when a new object is created
        self.borrow_counter = create_borrow_counter()

    def borrow_book(self):
        global total_books_in_library
        if total_books_in_library <= 0:
            print("No books available")
            return 
        total_books_in_library -= 1
        self.books_borrowed += 1
        self.borrow_counter()
        print(f"{self.name} borrowed a book. Books borrowed: {self.books_borrowed}")

    def return_books(self):
        global total_books_in_library
        if self.books_borrowed <= 0:
            print("No books to return")
            return
        
        self.books_borrowed -= 1
        total_books_in_library += 1
        print(f"{self.name} returned a book. Books borrowed: {self.books_borrowed}")

    def display_user_info(self):
        print(f"{self.name} has borrowed {self.books_borrowed} books")

    def display_total_user(self):
        print(self.total_user)

    @classmethod
    def disp(cls):
        print(cls.total_user)


user1 = libraryUser("Gautam")
user2 = libraryUser("Abhinav")

user1.borrow_book()
user1.borrow_book()
user1.borrow_book()
user1.borrow_book()

user2.borrow_book()
user2.borrow_book()

user1.display_user_info()
user2.display_user_info()

user1.display_total_user()
user1.disp()
libraryUser.disp()