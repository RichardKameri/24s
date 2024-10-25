import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables for books and members
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT NOT NULL UNIQUE,
    is_borrowed INTEGER NOT NULL DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    member_id TEXT NOT NULL UNIQUE
)
''')

conn.commit()
conn.close()


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"Member {self.name}, ID: {self.member_id}"

class Library:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def add_book(self, book):
        self.cursor.execute('INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)', (book.title, book.author, book.isbn))
        self.conn.commit()
        print(f"Added book: {book}")

    def register_member(self, member):
        self.cursor.execute('INSERT INTO members (name, member_id) VALUES (?, ?)', (member.name, member.member_id))
        self.conn.commit()
        print(f"Registered member: {member}")

    def borrow_book(self, isbn, member_id):
        self.cursor.execute('SELECT id, is_borrowed FROM books WHERE isbn = ?', (isbn,))
        book = self.cursor.fetchone()
        if book and not book[1]:
            self.cursor.execute('UPDATE books SET is_borrowed = 1 WHERE id = ?', (book[0],))
            self.conn.commit()
            print(f"Book {isbn} borrowed by member {member_id}")
        else:
            print(f"Book {isbn} is not available.")

    def return_book(self, isbn):
        self.cursor.execute('SELECT id FROM books WHERE isbn = ?', (isbn,))
        book = self.cursor.fetchone()
        if book:
            self.cursor.execute('UPDATE books SET is_borrowed = 0 WHERE id = ?', (book[0],))
            self.conn.commit()
            print(f"Book {isbn} returned")
        else:
            print(f"Book {isbn} not found.")

    def __del__(self):
        self.conn.close()


def main():
    library = Library()

    while True:
        print("\n1. Add Book\n2. Register Member\n3. Borrow Book\n4. Return Book\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.register_member(member)
        elif choice == '3':
            isbn = input("Enter book ISBN to borrow: ")
            member_id = input("Enter member ID: ")
            library.borrow_book(isbn, member_id)
        elif choice == '4':
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
