# Функция для поиска индекса товара
def product_index_search (items_list, product):
    if product in items_list: # Проверяем, есть ли товар в списке
        ans = items_list.index(product) # Получаем индекс первого вхождения товара
        return ans
    else: # Товара в списке нет
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = product_index_search(items_list, find_item)  # Вызов функции, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
