"""
Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
Пол: пол".
"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"

# пример использования
man = Person("Иван", 30, "мужчина")
print(man.info())  # выводит "name: Иван, age: 30, gender: мужчина"
