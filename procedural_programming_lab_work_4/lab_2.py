# Импортировать необходимые модули
import csv
import json
import sys


# Имена файлов ввода и вывода
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

# конвертации CSV в JSON
def task() -> None:
    # Считать содержимое csv файла
    try:
        # Открытие файла CSV для чтения
        with open(INPUT_FILENAME, newline='') as csvfile:
            # Создание объекта DictReader для чтения CSV файла
            reader = csv.DictReader(csvfile)
            # Преобразование данных в список словарей
            data = list(reader)
    except Exception as e:
        # Обработка исключения, если файл не найден
        print("Ошибка при открытии файла CSV")
        return e

    # Сериализовать в файл с отступами равными 4
    try:
        # Открытие файла JSON для записи
        with open(OUTPUT_FILENAME, 'w') as jsonfile:
            # Сериализация данных в JSON и запись в файл
            json.dump(data, jsonfile, indent=4)
    except Exception as e:
        # Обработка исключения при возникновении ошибок записи в файл JSON
        print("Ошибка при записи в файл JSON")
        return e


if __name__ == '__main__':
    # Запуск задачи конвертации
    task()

    # Вывод содержимого созданного JSON файла для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
