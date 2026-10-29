from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, speed, capacity):
        self.name = name         
        self.speed = speed        
        self.capacity = capacity  

    @abstractmethod
    def move(self, distance):
        """Час у дорозі у годинах"""
        pass

    @abstractmethod
    def fuel_consumption(self, distance):
        """Витрати пального"""
        pass

    def info(self):
        return f"{self.name}: швидкість {self.speed} км/год, місць: {self.capacity}"

    def calculate_cost(self, distance, price_per_unit):
        """Загальні витрати в грошах"""
        return self.fuel_consumption(distance) * price_per_unit


class Car(Transport):
    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return distance * 0.07  


class Bus(Transport):
    def __init__(self, name, speed, capacity, passengers=0):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        if self.passengers > self.capacity:
            return "Перевантажено!"  
        return distance * 0.15  


class Bicycle(Transport):
    def __init__(self, name, capacity=1):
        super().__init__(name, 20, capacity)

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return 0  


class ElectricCar(Car):
    def battery_usage(self, distance):
        return distance * 0.2  

    def fuel_consumption(self, distance):
        return 0  


if __name__ == "__main__":
    transports = [
        Car("Легкова машина", 120, 5),
        Bus("Автобус", 80, 40, passengers=35),
        Bus("Переповнений автобус", 80, 40, passengers=50),
        Bicycle("Велосипед"),
        ElectricCar("Tesla", 200, 5),
    ]

    distance = 100  

    for t in transports:
        time = t.move(distance)
        fuel = t.fuel_consumption(distance)
        print(f"{t.info()}")
        print(f"  Час на {distance} км: {time:.2f} год")
        print(f"  Витрати пального: {fuel}")
        print()

    car = Car("Моя машина", 120, 5)
    cost = car.calculate_cost(100, 55)  # 55 грн за літр
    print(f"Вартість поїздки на 100 км для авто: {cost:.2f} грн")

    tesla = ElectricCar("Tesla", 200, 5)
    print(f"Tesla на 100 км використає {tesla.battery_usage(100)}% батареї")