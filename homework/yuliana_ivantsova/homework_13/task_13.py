import os
import datetime

dir_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(dir_path))
data_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(data_path, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            yield line


def datetime_reader(line):
    line_part = line.strip().split()

    numer_line = line_part[0].rstrip('.')
    date_str = ' '.join(line_part[1:3])

    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if numer_line == '1':
            new_data = date + datetime.timedelta(weeks=1)
            print(f"Дата через неделю: {new_data}")

        elif numer_line == '2':
            day_index = date.strftime('%A')
            print(f"День недели: {day_index}")

        elif numer_line == '3':
            days_ago = (datetime.datetime.now() - date).days
            print(f"Дней прошло: {days_ago}")

    except ValueError as e:
        print(f"Ошибка парсинга даты: {e}")


def process_dates():

    for line in read_file():
        datetime_reader(line)


if __name__ == "__main__":
    process_dates()
