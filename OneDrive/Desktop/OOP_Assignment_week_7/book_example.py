class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        print(f"You read {pages} pages. Now on page {self.current_page} of '{self.title}'.")

    def bookmark(self, page):
        if 1 <= page <= self.pages:
            self.current_page = page
            print(f"Bookmarked page {page} in '{self.title}'.")
        else:
            print("Invalid page number.")

    def info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages, File size: {self.file_size}MB (E-Book)")

    def download(self):
        print(f"Downloading '{self.title}'... Done!")

# Example usage:
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 328)
    ebook = EBook("Digital Fortress", "Dan Brown", 356, 2.5)
    book.info()
    book.read(30)
    book.bookmark(100)
    ebook.info()
    ebook.download()
    ebook.read(50) 