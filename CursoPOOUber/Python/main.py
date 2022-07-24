from car import Car
from account import Account

if __name__== "__main__":
    print("Hola Mundo")

    car = Car("AMS145", Account("Andres Herrera", "1236552045"))
    print(vars(car))
    print(vars(car.driver))