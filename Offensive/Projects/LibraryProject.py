class Book:
    def __init__(self, id, author, name) -> None:
        self.id = id
        self.author = author
        self.name = name
        self.lent = False
        
    def __str__(self) -> str:
        return f"(Book id: {self.id}, Author: {self.author}, Book name: {self.name}, Lent: {self.lent})"
    
    def __repr__(self):
        return self.__str__()
        
     
class Libary:
    def __init__(self) -> None:
        self.books = {} # {1: book(1, ...), ...}
        
    def add_book(self, book):   
        if book.id not in self.books: 
            self.books[book.id] = book
        else:
            print(f"\n[!] Couldn't add that book becuase the id: {book.id} is already stored. ")
                
    @property
    def show_books(self):   
        return [book for book in self.books.values() if not book.lent]
    
    
    @property
    def show_lent_books(self):   
        return [book for book in self.books.values() if book.lent]
    
    def lend_book(self, id):
        if id in self.books.keys():
            if self.books[id].lent:
                print("Book already lent!")
            else:    
                self.books[id].lent = True
                print("Success!")
        else:
            print("\n[!] Couldn't find that book id!")
            
class ChildLibrary(Libary):
    def __init__(self):
        super().__init__()
        self.children_books = {} # -> {1: True, False, ...}
    
    def add_book(self, book, for_kids):
            super().add_book(book)
            self.children_books[book.id] = for_kids   

    def lend_book(self, id, for_kids):
        if id in self.books.keys() and not self.books[id].lent and self.children_books[id] == for_kids:
            self.books[id].lent = True
            print("Success!")
        else:
            print("\n[!] Couldn't lend that book!")
            
    @property
    def show_book_status(self):
        return self.children_books
                 
        
        
def main():
    
    library = ChildLibrary()  
    book1 = Book(1, "Jean", "0 Techniques")
    book2 = Book(2, "Val", "Auto")
    library.add_book(book1, for_kids = False)
    library.add_book(book2, for_kids = True) 
    
    print(f"\n[+] Library books:\n{library.show_books}")
    library.lend_book(1, for_kids = True)
    print(f"\n[+] Library books:\n{library.show_books}")
    library.lend_book(2)
    print(f"\n[+] Library books:\n{library.show_books}")
    print(f"\n[+] Library lent books:\n{library.show_lent_books}")
     
    print(library.show_book_status)


if __name__ == "__main__":
    main()