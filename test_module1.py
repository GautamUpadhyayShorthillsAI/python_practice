from module1 import Library
import unittest

class TestModule1(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        result = self.library.add_book("The Great Gatsby")
        self.assertEqual(result, "'The Great Gatsby' has been added to the library.")
        self.assertIn("The Great Gatsby", self.library.books)

    def test_add_existing_book(self):
        self.library.add_book("1984")
        res = self.library.add_book("1984")

        self.assertEqual(res,"'1984' is already in the library.")

    def test_issue_book(self):
        """Test issuing a book to a user."""
        self.library.add_book("Moby Dick")
        result = self.library.issue_book("Moby Dick", "John Doe")
        self.assertEqual(result, "'Moby Dick' has been issued to John Doe.")
        self.assertIn("Moby Dick", self.library.borrowed_books)

    def test_issue_book_not_available(self):
        """Test issuing a book that is not available."""
        result = self.library.issue_book("Unknown Book", "Jane Doe")
        self.assertEqual(result, "'Unknown Book' is not available in the library.")

    def test_return_book(self):
        """Test returning a borrowed book."""
        self.library.add_book("Pride and Prejudice")
        self.library.issue_book("Pride and Prejudice", "Alice")
        result = self.library.return_book("Pride and Prejudice")
        self.assertEqual(result, "'Pride and Prejudice' has been returned by Alice and added back to the library.")
        self.assertNotIn("Pride and Prejudice", self.library.borrowed_books)

    def test_return_book_not_borrowed(self):
        """Test returning a book that was not borrowed."""
        result = self.library.return_book("The Catcher in the Rye")
        self.assertEqual(result, "'The Catcher in the Rye' was not borrowed.")

    def test_check_availability(self):
        """Test checking the availability of a book."""
        self.library.add_book("To Kill a Mockingbird")
        result = self.library.check_availability("To Kill a Mockingbird")
        self.assertEqual(result, "'To Kill a Mockingbird' is available in the library.")

    def test_check_availability_borrowed(self):
        """Test checking availability of a borrowed book."""
        self.library.add_book("The Hobbit")
        self.library.issue_book("The Hobbit", "Bob")
        result = self.library.check_availability("The Hobbit")
        self.assertEqual(result, "'The Hobbit' is currently borrowed.")


if __name__ == "__main__":
    unittest.main()