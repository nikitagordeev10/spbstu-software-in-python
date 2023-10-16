list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Разделите участников на две команды
players_count = len(list_players)
team_1 = list_players[0:players_count // 2]
team_2 = list_players[players_count // 2:]

print(f'{team_1}\n{team_2}')
