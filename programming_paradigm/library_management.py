# Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), 
# return_book(title), and list_available_books.
class Book:
    def __init__(self,title,author):
        self.title= title
        self.author=author
        self.is_checked_out = False
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out= False
    def check_out_book(self):
        if not self.is_checked_out:
            self.is_checked_out= True 

class Library:
    def __init__(self):
        self._books=[]

    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_checked_out == False:
                print(f'{book.title} by {book.author}')

    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                book.return_book()                                              