class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author) 
        self.file_size = file_size   

class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author) 
        self.page_count = page_count 
class Library:
    books_list = []
    def __init__(self,books):
        self.books = books

    def add_book(self, book):
        return book
    
    def list_books(self):




my_library = Library()
classic_book = Book("Pride and Prejudice", "Jane Austen")
my_library.add_book(classic_book)
my_library.list_books()

if __name__ == "__main__":
    main()