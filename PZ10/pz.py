"""
В магазинах имеются следующие товары. 
Магнит – молоко, соль, сахар. Пятерочка – мясо, молоко, сыр. 
Перекресток – молоко, творог, сыр, сахар. 
Определить: 
1. в каких магазинах нельзя приобрести сыр. 
2. в каких магазинах можно приобрести
"""
magnit = {"молоко", "соль", "сахар"}
pyaterka = {"мясо", "молоко", "сыр"}
perecrestok = {"молоко", "творог", "сыр", "сахар"}

# 1. В каких магазинах нельзя приобрести сыр
no_cheese = {"Магнит" if "сыр" not in magnit else None,
             "Пятерочка" if "сыр" not in pyaterka else None,
             "Перекресток" if "сыр" not in perecrestok else None}
no_cheese.discard(None)  # Убираем None из результата

# 2. В каких магазинах можно приобрести одновременно молоко и сахар
milk_and_sugar = {"Магнит" if {"молоко", "сахар"}.issubset(magnit) else None,
                  "Пятерочка" if {"молоко", "сахар"}.issubset(pyaterka) else None,
                  "Перекресток" if {"молоко", "сахар"}.issubset(perecrestok) else None}
milk_and_sugar.discard(None)

# 3. В каких магазинах можно приобрести соль
have_salt = {"Магнит" if "соль" in magnit else None,
             "Пятерочка" if "соль" in pyaterka else None,
             "Перекресток" if "соль" in perecrestok else None}
have_salt.discard(None)

print("Нет сыра: " + ', '.join(no_cheese))
print("Есть молоко и сахар: " + ', '.join(milk_and_sugar))
print("Есть соль: " + ', '.join(have_salt))