"""EXT 1:
Create a Book class that lets you create books with a title, author, and price.
Then create a Shelf class, onto which you can place one or more books with an
add_book method. Finally, add a total_price method to the Shelf class, which
will total the prices of the books on the shelf.
"""

"""EXT 2:
Write a method, Shelf.has_book, that takes a single string argument and
returns True or False, depending on whether a book with the named title
exists on the shelf.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price



class Shelf:
    def __init__(self):
        self.list_of_books = []

    def add_book(self, *books):
        self.list_of_books.extend(books)
        # Reuven utiliza esto... que es equivalente a extend
        # self.list_of_books += books
        # Porque la suma de dos listas (o más) es la lista que contiene todo__ es como unirlas!!

    def total_price(self):
        return sum(book.price for book in self.list_of_books)

    def __repr__(self):
        return '\n'.join(book.title
                         for book in self.list_of_books)


    def has_book_v0(self, title):
        # Para la extensión 2
        for book in self.list_of_books:
            if title == book.title:
                return True

        return False

    def has_book_v1(self, title):
        return any(title == book.title for book in self.list_of_books)

    def has_book_v2(self, title):
        # Esta es la mejor,... aunque la pensé yo por mi cuenta
        # también, lógicamente, es la que usa Reuven
        return title in (book.title for book in self.list_of_books)


if __name__ == '__main__':
    book_1 = Book('Harry Potter', 'JK Rowling', 17)
    book_2 = Book('Africanus', 'Santiago Posteguillo', 23)
    book_3 = Book('Invisible', 'ELoy Moreno', 12)
    book_4 = Book('Misterio en el Orient Express', 'Agatha Christie', 8)

    shelf = Shelf()
    shelf.add_book(book_1)
    shelf.add_book(book_2, book_3, book_4)
    print(shelf)
    print(shelf.total_price())



