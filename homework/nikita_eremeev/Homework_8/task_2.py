import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for index, number in enumerate(fibonacci_generator(), start=1):
    if index == 5:
        print(f"5-е число: {number}")
    elif index == 200:
        print(f"200-е число: {number}")
    elif index == 1000:
        print(f"1000-е число: {number}")
    elif index == 100000:
        print(f"100000-е число: {number}")
        break
