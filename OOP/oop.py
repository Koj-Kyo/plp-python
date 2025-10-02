# Assignment 1: Design Your Own Class! 🏗️


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        return f"You start reading '{self.title}'."

class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb

    def description(self):
        return f"'{self.title}' (eBook) by {self.author}, {self.pages} pages, {self.file_size_mb}MB."

    def download(self):
        return f"Downloading '{self.title}' ({self.file_size_mb}MB)..."

# Example usage
physical_book = Book("1984", "George Orwell", 328)
ebook = EBook("Digital Fortress", "Dan Brown", 356, 2)

print(physical_book.description())
print(physical_book.read())
print(ebook.description())
print(ebook.download())

