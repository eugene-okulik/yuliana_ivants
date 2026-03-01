import argparse
import os
from collections import defaultdict

from colorama import init, Fore

init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("path", help="directory")
parser.add_argument("-d", "--date", help="data for search")
parser.add_argument("--text", help="text for search")
args = parser.parse_args()
print(args.path, args.text)


def get_files_list(path_string):

    files_list = []
    if os.path.isfile(path_string):
        files_list.append(path_string)
    elif os.path.isdir(path_string):
        for root, __, files in os.walk(path_string):
            for file in files:
                full_path = os.path.join(root, file)
                files_list.append(full_path)
    else:
        raise ValueError("Путь не существует")

    return files_list


def search_in_files(search_text):
    files = get_files_list(args.path)
    blocks = defaultdict(list)
    for file in files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                parts = line.strip().split()

                time_key = parts[0]

                blocks[time_key].append((line_number, line.strip()))

        # Поиск внутри блоков
        for time_key, messages in blocks.items():
            for line_number, line in messages:
                if search_text.lower() in line.lower():
                    print_result(
                        line_number, line, file, search_text, time_key
                    )


def print_result(line_number, line, file, text_search, time_key):

    words = line.split()

    for i, word in enumerate(words):
        if text_search.lower() in word.lower():

            start = max(0, i - 1)
            end = min(len(words), i + 6)

            fragment = " ".join(words[start:end])
            print(
                Fore.BLUE + "Файл:", file,
                Fore.MAGENTA + "Время:", time_key,
                Fore.CYAN + "Строка:", str(line_number),
                Fore.GREEN + "Фрагмент:", fragment
            )


search_in_files(args.text)
