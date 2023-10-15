users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# Добавьте словарь и замените в нем нулевые значения статисчикой посещений
site_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

site_statistics["Общее количество"] = len(users)
site_statistics["Уникальные посещения"] = len(set(users))

print(site_statistics)
