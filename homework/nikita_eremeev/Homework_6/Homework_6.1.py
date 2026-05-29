text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()
new_words = []

for word in words:
    # Проверяем, есть ли знак препинания в конце слова
    if word[-1] in ',.':
        punctuation = word[-1]  # запятая или точка
        clean_word = word[:-1]  # слово без знака препинания
        new_word = clean_word + 'ing' + punctuation
    else:
        new_word = word + 'ing'

    new_words.append(new_word)

result = ' '.join(new_words)
print(result)
