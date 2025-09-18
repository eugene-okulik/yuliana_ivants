def generator_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_num_from_fibonacci(num):

    fib_generator = generator_fibonacci()
    for i in range(num + 1):
        result = next(fib_generator)
    return result


print(f"Пятое число из ряда Фибоначчи: {get_num_from_fibonacci(4)}")
print(f"Двухсотое число из ряда Фибоначчи: {get_num_from_fibonacci(199)}")
print(f"Тысячное число из ряда Фибоначчи: {get_num_from_fibonacci(999)}")
print(f"Стотысячное число из ряда Фибоначчи: {get_num_from_fibonacci(9999)}")
