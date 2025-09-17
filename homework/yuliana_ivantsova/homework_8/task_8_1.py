import random

salary = int(input("Введите желаемую заработную плату: "))

def assigning_bonus(salary):

    bonus = random.choice([True, False])

    if bonus:
        salary += random.randint(1, 1000)
    else:
        print("Бонус не получен, увы")

    return salary, bonus

new_salary, bonus = assigning_bonus(salary)
print(f"{salary}, {bonus} - '${new_salary}'")
