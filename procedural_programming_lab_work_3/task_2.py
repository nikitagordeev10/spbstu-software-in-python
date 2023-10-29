# Функция поиска общих участников
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников, используя заданный разделитель
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Преобразуем списки в множества для быстрого поиска общих участников
    set1 = set(participants1)
    set2 = set(participants2)

    # Находим общих участников, используя операцию пересечения множеств
    common_participants = set1.intersection(set2)

    # Преобразуем множество общих участников обратно в список и сортируем его
    sorted_common_participants = list(common_participants)
    sorted_common_participants.sort()

    return sorted_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))




