"""EXT 3
Modify your Book class such that it adds another attribute, width. Then add a
width attribute to each instance of Shelf. When add_book tries to add books
whose combined widths will be too much for the shelf, raise an exception"""



class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

class EspacioInsuficiente(Exception):
    pass

class Shelf:
    def __init__(self, width):
        self.list_of_books = []
        self.width = width
        self.width_of_books_on_shelf = 0

    def add_book(self, *books):
        # Cambio la implementación después de ver Reuven...
        # conviene ir poco a poco de uno a uno añadiendo los libros
        # por si no cupieran todos, al menos añadir los que se puedan!!!
        for new_book in books:
            if self.width_of_books_on_shelf + new_book.width > self.width:
                raise EspacioInsuficiente('Lo siento, ya no queda espacio en el estante')
            self.list_of_books.append(new_book)
            self.width_of_books_on_shelf += new_book.width


    def total_price(self):
        return sum(book.price for book in self.list_of_books)

    def __repr__(self):
        return '\n'.join(book.title for book in self.list_of_books) + \
                f'\nEl grosor del estante es de {self.width} de los que están ocupados {self.width_of_books_on_shelf}'




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
    book_1 = Book('Harry Potter', 'JK Rowling', 17, 24)
    book_2 = Book('Africanus', 'Santiago Posteguillo', 23, 24)
    book_3 = Book('Invisible', 'ELoy Moreno', 12, 24)
    book_4 = Book('Misterio en el Orient Express', 'Agatha Christie', 8, 24)

    shelf = Shelf(80)
    print(0)
    shelf.add_book(book_1)
    print(1)
    shelf.add_book(book_2, book_3, book_4)
    print(2)
    # shelf.add_book(book_4)
    print(shelf)
    print(shelf.total_price())