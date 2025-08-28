result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
digit_1 = int(result_1[result_1.index(': ') + 1:])
digit_2 = int(result_2[result_2.index(': ') + 1:])
digit_3 = int(result_3[result_3.index(': ') + 1:])
print(digit_1)
print(digit_2)
print(digit_3)
