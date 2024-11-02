class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book title: {self.title} \nAuthor: {self.author} \nNumber of pages: {self.pages}"


    def __len__(self):
        return self.pages


book1 = Book("Lammer", "Silv", 23)
print(book1)
print(len(book1))