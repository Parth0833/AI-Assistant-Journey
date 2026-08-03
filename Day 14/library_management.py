# Parent Class
class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


# Child Class 1
class ScienceBook(Book):

    def __init__(self, title, author, isbn, field_of_science):
        super().__init__(title, author, isbn)
        self.field_of_science = field_of_science

    def display_info(self):
        base_info = super().display_info()
        return f"[Science - {self.field_of_science}] {base_info}"


# Child Class 2
class StoryBook(Book):

    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def display_info(self):
        base_info = super().display_info()
        return f"[Story - {self.genre}] {base_info}"


# Example Usage
if __name__ == "__main__":
    sci_book = ScienceBook(
        "A Brief History of Time",
        "Stephen Hawking",
        "978-0553380163",
        "Physics",
    )
    story_book = StoryBook(
        "Harry Potter", "J.K. Rowling", "978-0439708180", "Fantasy"
    )

    print(sci_book.display_info())
    print(story_book.display_info())