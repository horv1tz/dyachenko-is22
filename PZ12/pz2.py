def to_uppercase_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char.upper()
        else:
            yield char

# Пример использования генератора
input_string = "Привет, как дела?"
uppercase_string = ''.join(to_uppercase_generator(input_string))
print(uppercase_string)
