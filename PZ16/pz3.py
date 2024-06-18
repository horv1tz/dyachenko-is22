"""
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""

import pickle

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"

def save_def(filename, persons):
    """Сохраняет список объектов Person в файл."""
    with open(filename, 'wb') as file:
        pickle.dump(persons, file)

def load_def(filename):
    """Загружает список объектов Person из файла."""
    with open(filename, 'rb') as file:
        persons = pickle.load(file)
    return persons

# Пример использования
# Создаем три экземпляра класса Person
person1 = Person("Иван", 30, "мужчина")
person2 = Person("Мария", 25, "женщина")
person3 = Person("Алексей", 40, "мужчина")

# Сохраняем объекты в файл
persons_list = [person1, person2, person3]
save_def('persons.pkl', persons_list)
fd
# Загружаем объекты из файла
loaded_persons = load_def('persons.pkl')

# Выводим информацию о загруженных людях
for person in loaded_persons:
    print(person.info())
