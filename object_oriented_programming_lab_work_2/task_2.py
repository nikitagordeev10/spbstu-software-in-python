# класс Book
class Book:
    """
    Класс, описывающий книгу
    """
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Метод, возвращающий строковое представление объекта Book
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод, возвращающий строку, показывающую как может быть инициализирован экземпляр
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# класс Library
class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library, инициализирует список книг библиотеки
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод возвращает следующий уникальный идентификатор для новой книги в библиотеке
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод возвращает индекс книги в списке библиотеки по заданному идентификатору
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
