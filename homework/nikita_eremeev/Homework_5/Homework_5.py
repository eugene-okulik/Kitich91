person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Первая строка
result1 = "результат операции: 42"
num1 = int(result1[result1.index(':') + 1:].strip())
print(num1 + 10)

# Вторая строка
result2 = "результат операции: 514"
num2 = int(result2[result2.index(':') + 1:].strip())
print(num2 + 10)

# Третья строка
result3 = "результат работы программы: 9"
num3 = int(result3[result3.index(':') + 1:].strip())
print(num3 + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

print(f"Students {students_str} study these subjects: {subjects_str}")
