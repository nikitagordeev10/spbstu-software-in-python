from typing import Union

class Car:
    """Базовый класс, представляющий общий автомобиль."""

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализирует объект Car.

        Args:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год производства автомобиля.
        """
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self) -> str:
        """Марка автомобиля."""
        return self._brand

    @property
    def model(self) -> str:
        """Модель автомобиля."""
        return self._model

    @property
    def year(self) -> int:
        """Год производства автомобиля."""
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        """Устанавливает год производства автомобиля."""
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            raise ValueError("Год должен быть положительным целым числом.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        Returns:
            str: Строковое представление автомобиля.
        """
        return f"{self._year} {self._brand} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление автомобиля для воссоздания объекта.

        Returns:
            str: Строковое представление автомобиля.
        """
        return f"Car(brand={self._brand}, model={self._model}, year={self._year})"


class PassengerCar(Car):
    """Класс, представляющий легковой автомобиль, наследуемый от Car."""

    def __init__(self, brand: str, model: str, year: int, passengers: int):
        """
        Инициализирует объект PassengerCar.

        Args:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год производства автомобиля.
            passengers (int): Максимальное количество пассажиров.
        """
        super().__init__(brand, model, year)
        self._passengers = passengers

    @property
    def passengers(self) -> int:
        """Максимальное количество пассажиров."""
        return self._passengers

    @passengers.setter
    def passengers(self, passengers: int) -> None:
        """Устанавливает максимальное количество пассажиров."""
        if isinstance(passengers, int) and passengers > 0:
            self._passengers = passengers
        else:
            raise ValueError("Количество пассажиров должно быть положительным целым числом.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        Returns:
            str: Строковое представление легкового автомобиля.
        """
        return f"{super().__str__()}, Максимальное количество пассажиров: {self._passengers}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля для воссоздания объекта.

        Returns:
            str: Строковое представление легкового автомобиля.
        """
        return f"PassengerCar(brand={self._brand}, model={self._model}, year={self._year}, passengers={self._passengers})"

    def load_passengers(self, num_passengers: int) -> str:
        """
        Посадка пассажиров в автомобиль.

        Args:
            num_passengers (int): Количество пассажиров для посадки.

        Returns:
            str: Сообщение о результате операции посадки пассажиров.
        """
        if num_passengers <= self._passengers:
            return f"{num_passengers} пассажиров сели в автомобиль."
        else:
            return "Невозможно посадить пассажиров. Превышено максимальное количество."


class Truck(Car):
    """Класс, представляющий грузовик, наследующий от Car."""

    def __init__(self, brand: str, model: str, year: int, payload_capacity: Union[float, int]):
        """
        Инициализирует объект Truck.

        Args:
            brand (str): Марка грузовика.
            model (str): Модель грузовика.
            year (int): Год производства грузовика.
            payload_capacity (Union[float, int]): Максимальная грузоподъемность грузовика.
        """
        super().__init__(brand, model, year)
        self._payload_capacity = payload_capacity

    @property
    def payload_capacity(self) -> Union[float, int]:
        """Максимальная грузоподъемность грузовика."""
        return self._payload_capacity

    @payload_capacity.setter
    def payload_capacity(self, payload_capacity: Union[float, int]) -> None:
        """Устанавливает максимальную грузоподъемность грузовика."""
        if isinstance(payload_capacity, (float, int)) and payload_capacity > 0:
            self._payload_capacity = payload_capacity
        else:
            raise ValueError("Грузоподъемность должна быть положительным числом.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузовика.

        Returns:
            str: Строковое представление грузовика.
        """
        return f"{super().__str__()}, Грузоподъемность: {self._payload_capacity} тонн"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление грузовика для воссоздания объекта.

        Returns:
            str: Строковое представление грузовика.
        """
        return f"Truck(brand={self._brand}, model={self._model}, year={self._year}, payload_capacity={self._payload_capacity})"

    def transport_goods(self, weight: Union[float, int]) -> str:
        """
        Транспортирует грузы грузовиком.

        Args:
            weight (Union[float, int]): Вес груза для транспортировки.

        Returns:
            str: Сообщение о результате операции транспортировки груза.
        """
        if weight <= self._payload_capacity:
            return f"Груз успешно транспортирован. Вес: {weight} тонн"
        else:
            return "Невозможно транспортировать груз. Превышена грузоподъемность."



# Создание экземпляра легкового автомобиля
passenger_car = PassengerCar("Toyota", "Corolla", 2022, 5)

# Изменение года производства легкового автомобиля с помощью setter
passenger_car.year = 2023

# Посадка пассажиров в легковой автомобиль
result = passenger_car.load_passengers(4)
print(result)  # Вывод: "4 пассажиров сели в автомобиль."

# Создание экземпляра грузовика
truck = Truck("Volvo", "FH16", 2020, 20)

# Попытка установить некорректное значение года производства грузовика
try:
    truck.year = -2021
except ValueError as e:
    print(e)  # Вывод: "Год должен быть положительным целым числом."

# Попытка установить некорректное значение грузоподъемности грузовика
try:
    truck.payload_capacity = -25
except ValueError as e:
    print(e)  # Вывод: "Грузоподъемность должна быть положительным числом."

# Перевозка груза грузовиком
result = truck.transport_goods(15)
print(result)  # Вывод: "Груз успешно транспортирован. Вес: 15 тонн."