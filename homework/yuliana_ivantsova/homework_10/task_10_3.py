digital_first = int(input("Введите число:  "))
digital_second = int(input("Введите число:  "))


def operation_calc(func):

    def wrapper(first, second):

        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        result = func(first, second, operation)
        return result
    return wrapper


@operation_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Неизвестная операция"


result = calc(digital_first, digital_second)
print(result)
