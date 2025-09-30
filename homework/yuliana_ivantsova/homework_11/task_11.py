
class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, name, author, count_pages, isbn, reserve):
        self.name = name
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserve = reserve

    def print_books(self):
        if self.reserve:
            print(
                f"Название: {self.name}, "
                f"Автор: {self.author}, страниц: {self.count_pages}, "
                f"материал: {self.page_material}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.name}, Автор: {self.author}, "
                f"страниц: {self.count_pages}, материал: {self.page_material}"
            )


book_one = Book("It", "King", 1200, "5558", True)
book_two = Book("Pride and Prejudice", "Ostin", 500, "5658", False)
book_three = Book("Guards! Guards!", "Pratchett", 600, "8797", False)
book_four = Book("Ген Рафаила", "Качур", 500, "7787", False)
book_five = Book("Два капитана", "Каверин", 1200, "8582", False)

book_list = [book_one, book_two, book_three, book_four, book_five]
for book in book_list:
    book.print_books()


class SchoolBook(Book):

    def __init__(
            self, name, author, count_pages, isbn,
            reserve, subject, class_room, task
    ):
        super().__init__(name, author, count_pages, isbn, reserve)
        self.subject = subject
        self.class_room = class_room
        self.task = task

    def print_school_books(self):
        if self.reserve:
            print(
                f"Название: {self.name}, "
                f"Автор: {self.author}, страниц: {self.count_pages}, "
                f"предмет: {self.subject}, "
                f"материал: {self.page_material}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.name}, Автор: {self.author}, "
                f"страниц: {self.count_pages}, материал: {self.page_material}"
            )


school_book_one = SchoolBook(
    "Алгебра", "Иванов", 200, "978", True,
    "Математика", 9, True
                             )
school_book_two = SchoolBook(
    "История России", "Петров", 300, "9788", False,
    "История", 10, True
                             )
school_book_three = SchoolBook(
    "География", "Сидоров", 250, "97873", False,
    "География", 8, False
                             )
school_book_four = SchoolBook(
    "Физика", "Кузнецов", 350, "97844", False, "Физика",
    11, True
                             )
school_book_five = SchoolBook(
    "Биология", "Васильев", 280, "97855", False,
    "Биология", 7, True
                             )

book_school_list = [
    school_book_one, school_book_two, school_book_three,
    school_book_four, school_book_five
]
for book in book_school_list:
    book.print_school_books()
