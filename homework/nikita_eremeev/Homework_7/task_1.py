secret_number = 7  # Загаданное число (можно любое)

while True:
    user_input = input("Угадайте цифру: ")

    # Проверяем, что ввели именно число (опционально, но хорошая практика)
    if not user_input.isdigit():
        print("Пожалуйста, введите число!")
        continue

    guess = int(user_input)

    if guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
