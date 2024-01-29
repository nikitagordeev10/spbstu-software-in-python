class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # Атрибут name сделан приватным
        self._author = author  # Атрибут author сделан приватным

    @property
    def name(self):
        return self._name  # Свойство для доступа к атрибуту name

    @property
    def author(self):
        return self._author  # Свойство для доступа к атрибуту author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages  # Атрибут pages сделан приватным

    @property
    def pages(self):
        return self._pages  # Свойство для доступа к атрибуту pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value  # Проверка и установка значения атрибута pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration  # Атрибут duration сделан приватным

    @property
    def duration(self):
        return self._duration  # Свойство для доступа к атрибуту duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = value  # Проверка и установка значения атрибута duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
