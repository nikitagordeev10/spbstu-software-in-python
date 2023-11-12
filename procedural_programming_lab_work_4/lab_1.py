# Импортировать необходимые модули
import json

# Нахождение суммы произведений значений "score" и "weight" из JSON файла
def task() -> float:
    # Путь к файлу
    file_path = 'input.json'

    try:
        # Попытка открыть и прочитать файл JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        # Вывод сообщения об ошибке при чтении файла JSON
        print("Ошибка при чтении файла JSON")
        return e

    # Вычисление суммы произведений "score" и "weight" в каждом словаре
    sum_of_products = sum(item["score"] * item["weight"] for item in data)

    # Округление результата до трех знаков после запятой
    rounded_sum = round(sum_of_products, 3)

    return rounded_sum

if __name__ == '__main__':
    # Запуск задачи нахождения суммы
    print(task())
