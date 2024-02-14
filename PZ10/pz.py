# Переопределим множества товаров для каждого магазина более простым способом
shops = {
    "Магнит": {"молоко", "соль", "сахар"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар"}
}

# 1. В каких магазинах нельзя приобрести сыр
no_cheess = [shop for shop, things in shops.items() if "сыр" not in things]

# 2. В каких магазинах можно приобрести одновременно молоко и сахар
milk_and_sugar = [shop for shop, things in shops.items() if {"молоко", "сахар"}.issubset(things)]

# 3. В каких магазинах можно приобрести соль
have_sault = [shop for shop, things in shops.items() if "соль" in things]

print(no_cheess)
print(milk_and_sugar)
print(have_sault)