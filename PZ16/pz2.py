"""
Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать".
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дышит")

    def eat(self):
        print(f"{self.name} ест")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed # Порода

    def bark(self):
        print(f"{self.name} лает")

class Cat(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color # Цвет меха

    def purr(self):
        print(f"{self.name} мурлычет")

# example usage
dog = Dog("Bobby", "German Shepherd")
dog.breathe()  # outputs "Bobby дышит"
dog.eat()  # outputs "Bobby ест"
dog.bark()  # outputs "Bobby лает"

cat = Cat("Murry", "black")
cat.breathe()  # outputs "Murry дышит"
cat.eat()  # outputs "Murry ест"
cat.purr()  # outputs "Murry дышит"
