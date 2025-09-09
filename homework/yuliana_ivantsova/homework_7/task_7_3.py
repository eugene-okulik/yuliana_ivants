results = ['результат операции: 42', 'результат операции: 514', 'результат работы программы: 9', 'результат: 2']


def function(data_list):

    for result in data_list:
        digit = int(result.split(': ')[-1]) + 10
        print(digit)


function(results)
