import os
import datetime


current_dir = os.path.dirname(__file__)
base_dir = os.path.dirname(os.path.dirname(current_dir))
file_dir = os.path.join(base_dir, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(file_dir, 'r') as file:
        for line in file:
            datetime_reader(line)


def datetime_reader(line):
    line_path = line.strip().split()
    number_line = line_path[0].rstrip('.')
    date_str = ' '.join(line_path[1:3])

    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        if number_line == '1':
            new_data = date + datetime.timedelta(weeks=1)
            print(f"Дата через неделю: {new_data}")

        elif number_line == '2':
            day_index = date.strftime('%A')
            print(f"День недели: {day_index}")

        elif number_line == '3':
            days_ago = (datetime.datetime.now() - date).days
            print(f"Дней прошло: {days_ago}")

    except ValueError as e:
        print(f"Ошибка парсинга даты: {e}")


if __name__ == "__main__":
    read_file()
