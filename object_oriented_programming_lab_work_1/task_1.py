from typing import Union
# 3 класса с документацией и аннотацией типов
class Car:
    """
    Класс, описывающий автомобиль

    Атрибуты:
    - brand (str): Марка автомобиля
    - model (str): Модель автомобиля
    """

    def __init__(self, brand: str, model: Union[str, int]):
        if not brand or not model:
            raise ValueError("Марка и модель не должны быть пустыми")
        self.brand = brand
        self.model = model

    def start_engine(self):
        """
        Метод для запуска двигателя автомобиля

        Пример использования:
        >>> car = Car("Toyota", "Camry")
        >>> car.start_engine()
        Двигатель Toyota Camry запустился
        """
        print(f"Двигатель {self.brand} {self.model} запустился")

    def drive(self):
        """
        Метод для движения автомобиля

        Пример использования:
        >>> car = Car("Toyota", "Camry")
        >>> car.drive()
        Автомобиль Toyota Camry едет
        """
        print(f"Автомобиль {self.brand} {self.model} едет")

    def park(self):
        """
        Метод для парковки автомобиля

        Пример использования:
        >>> car = Car("Toyota", "Camry")
        >>> car.park()
        Автомобиль Toyota Camry припарковался
        """
        print(f"Автомобиль {self.brand} {self.model} припарковался")

class Airplane:
    """
    Класс, описывающий самолёт

    Атрибуты:
    - brand (str): Производитель самолёта
    - model (str): Модель самолёта
    """

    def __init__(self, brand: str, model: Union[str, int]):
        if not brand or not model:
            raise ValueError("Производитель и модель не должны быть пустыми")
        self.brand = brand
        self.model = model

    def take_off(self):
        """
        Метод для взлета самолёта.

        Пример использования:
        >>> airplane = Airplane("Boeing", "747")
        >>> airplane.take_off()
        Самолет Boeing 747 взлетел
        """
        print(f"Самолет {self.brand} {self.model} взлетел")

    def fly(self):
        """
        Метод для полёта самолёта.

        Пример использования:
        >>> airplane = Airplane("Boeing", "747")
        >>> airplane.fly()
        Самолет Boeing 747 летит
        """
        print(f"Самолет {self.brand} {self.model} летит")

    def land(self):
        """
        Метод для посадки самолёта

        Пример использования:
        >>> airplane = Airplane("Boeing", "747")
        >>> airplane.land()
        Самолет Boeing 747 приземлился
        """
        print(f"Самолет {self.brand} {self.model} приземлился")

class Ship:
    """
       Класс, описывающий корабль

       Атрибуты:
       - ship_type (str): Тип корабля
       - name (str): Название корабля
   """
    def __init__(self, ship_type: str, name: Union[str, int]):
        if not ship_type or not name:
            raise ValueError("Тип и название не должны быть пустыми")
        self.ship_type = ship_type
        self.name = name

    def sail(self):
        """
        Метод для плавания корабля.

        Пример использования:
        >>> ship = Ship("Ледокол", "Ямал")
        >>> ship.sail()
        Корабль Ледокол Ямал плывет
        """
        print(f"Корабль {self.ship_type} {self.name} плывет")

    def anchor(self):
        """
        Метод для опускания якоря корабля.

        Пример использования:
        >>> ship = Ship("Ледокол", "Ямал")
        >>> ship.anchor()
        Якорь опущен, корабль Ледокол Ямал стоит на якоре
        """
        print(f"Якорь опущен, корабль {self.ship_type} {self.name} стоит на якоре")

    def dock(self):
        """
        Метод для причаливания корабля.

        Пример использования:
        >>> ship = Ship("Ледокол", "Ямал")
        >>> ship.dock()
        Корабль Ледокол Ямал пришвартован
        """
        print(f"Корабль {self.ship_type} {self.name} пришвартован")


if __name__ == "__main__":
    # работоспособность экземпляров класса проверить с помощью doctest
    car = Car("Toyota", "Camry")
    car.start_engine()
    car.drive()
    car.park()

    airplane = Airplane("Boeing", "747")
    airplane.take_off()
    airplane.fly()
    airplane.land()

    ship = Ship("Ледокол", "Ямал")
    ship.sail()
    ship.anchor()
    ship.dock()
