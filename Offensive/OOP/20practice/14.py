from abc import ABC, abstractmethod

class LibraryItem(ABC):
    
    @abstractmethod
    def checkout(self):
        pass

class Book(LibraryItem):

    def checkout(self):
        return f"Book checked out!"

class Magazine(LibraryItem):

    def checkout(self):
        return f"Magazine checked out!"


book = Book()
print(book.checkout())
magazine = Magazine()
print(magazine.checkout())