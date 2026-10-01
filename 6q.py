from abc import ABC, abstractmethod


class Transport(ABC):
    """Абстрактний базовий клас транспорту."""

    def __init__(self, name: str, speed: int, capacity: int):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance: float) -> float:
        """Повертає час у дорозі (у годинах)."""
        ...

    @abstractmethod
    def fuel_consumption(self, distance: float) -> float:
        """Повертає витрати пального на дистанцію."""
        ...

    def calculate_cost(self, distance: float, price_per_unit: float) -> float:
        """Загальні витрати в грошах."""
        return self.fuel_consumption(distance) * price_per_unit

    @abstractmethod
    def info(self) -> str:
        ...


class Car(Transport):
    """Легковий автомобіль: 0.07 л/км."""

    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return distance * 0.07

    def info(self) -> str:
        return f"Автомобіль {self.name}, швидкість {self.speed} км/год, місць {self.capacity}"


class Bus(Transport):
    """Автобус: 0.15 л/км, перевірка перевантаження."""

    def __init__(self, name: str, speed: int, capacity: int, passengers: int = 0):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return distance * 0.15

    def info(self) -> str:
        if self.passengers > self.capacity:
            return f"Автобус {self.name}: Перевантажено! ({self.passengers}/{self.capacity})"
        return f"Автобус {self.name}, пасажирів {self.passengers}/{self.capacity}"


class Bicycle(Transport):
    """Велосипед: пального 0, швидкість не більше 20 км/год."""

    MAX_SPEED = 20

    def __init__(self, name: str, capacity: int = 1):
        super().__init__(name, speed=self.MAX_SPEED, capacity=capacity)

    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return 0.0

    def info(self) -> str:
        return f"Велосипед {self.name}, швидкість до {self.MAX_SPEED} км/год"


class ElectricCar(Car):
    """Електромобіль: батарея 0.2 кВт·год/км, пального немає."""

    def battery_usage(self, distance: float) -> float:
        return distance * 0.2

    def fuel_consumption(self, distance: float) -> float:
        return 0.0

    def calculate_cost(self, distance: float, price_per_unit: float) -> float:
        return self.battery_usage(distance) * price_per_unit

    def info(self) -> str:
        return f"Електромобіль {self.name}, швидкість {self.speed} км/год"


transports = [
    Car("Toyota Corolla", 120, 5),
    Bus("Богдан А092", 80, 35, passengers=40),  
    Bus("Еталон А081", 80, 35, passengers=20),
    Bicycle("Giant Escape"),
    ElectricCar("Tesla Model 3", 200, 5),
]

distance = 100

for t in transports:
    print(t.info())
    print(f"  Час на {distance} км: {t.move(distance):.2f} год")
    print(f"  Витрати: {t.fuel_consumption(distance):.2f}")
    print()


print("Вартість поїздки на 100 км (пальне 50 грн/л, електрика 8 грн/кВт·год):")
for t in transports:
    price = 8 if isinstance(t, ElectricCar) else 50
    print(f"  {t.name}: {t.calculate_cost(distance, price):.2f} грн")