import random

# Ввод зарплаты
salary = int(input("Введите вашу зарплату: "))

# Рандомно определяем, будет ли бонус (True или False)
bonus = random.choice([True, False])

if bonus:
    # Генерируем случайный бонус (например, от 100 до 5000)
    bonus_amount = random.randint(100, 5000)
    result = salary + bonus_amount
else:
    result = salary

print(f"${result}")
