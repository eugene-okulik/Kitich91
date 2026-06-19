def process_result(text):
    """Извлекает число из строки, прибавляет 10 и выводит результат"""
    # Способ 1: через split (проще)
    number = int(text.split(':')[-1])
    print(number + 10)

    # Способ 2: через index (если нужно по заданию)
    # number = int(text[text.index(':') + 2:])
    # print(number + 10)


# Список строк для обработки
results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

# Обрабатываем все строки без повторения кода
for result in results:
    process_result(result)
