class Vehicle:
    """Базовый класс, представляющий транспортное средство."""

    def __init__(self, brand: str, color: str):
        """
        Конструктор класса Vehicle.

        Аргументы:
        - brand: Марка транспортного средства.
        - color: Цвет транспортного средства.
        """
        self.brand = brand
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращаемое значение:
        Строковое представление объекта.
        """
        return f"{self.color} {self.brand}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для использования в REPL.

        Возвращаемое значение:
        Строковое представление объекта.
        """
        return f"Vehicle(brand={self.brand}, color={self.color})"

    def drive(self) -> None:
        """
        Метод, представляющий действие вождения.

        Не возвращает значения.
        """
        print(f"{self.brand} едет!")


class Car(Vehicle):
    """Дочерний класс Car, представляющий автомобиль."""

    def __init__(self, brand: str, color: str, max_speed: int):
        """
        Конструктор класса Car.

        Аргументы:
        - brand: Марка автомобиля.
        - color: Цвет автомобиля.
        - max_speed: Максимальная скорость автомобиля.
        """
        super().__init__(brand, color)
        self.max_speed = max_speed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращаемое значение:
        Строковое представление объекта.
        """
        return f"{self.color} {self.brand} (max_speed: {self.max_speed} km/h)"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для использования в REPL.

        Возвращаемое значение:
        Строковое представление объекта.
        """
        return f"Car(brand={self.brand}, color={self.color}, max_speed={self.max_speed})"

    def honk(self) -> None:
        """
        Метод, производящий звук автомобильного клаксона.

        Не возвращает значения.
        """
        print("Биб-бип!")


# Пример использования
vehicle = Vehicle("Toyota", "черный")
print(vehicle)      # черный Toyota
print(repr(vehicle))  # Vehicle(brand=Toyota, color=черный)
vehicle.drive()    # Toyota едет!

car = Car("BMW", "синий", 250)
print(car)          # синий BMW (max_speed: 250 km/h)
print(repr(car))    # Car(brand=BMW, color=синий, max_speed=250)
car.drive()        # BMW едет!
car.honk()         # Биб-бип!
