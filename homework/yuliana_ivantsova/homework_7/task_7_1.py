expected_num = 155
current_num = int(input("Испытайте удачу! Введите цифру..."))
print(current_num)
while current_num != expected_num:
    current_num = int(input("Попробуйте снова!..."))
print('Поздравляю! Вы угадали!')
