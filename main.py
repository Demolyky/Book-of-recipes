
def main():
    cook_book = reading_cook_book('Cookbook.txt')
    ingredient_for_cook = get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 2)
    # Для тренеровки работы с вложенными словарями сделал вывод
    for dish_name, ingredients in cook_book.items():
        print(f'{dish_name}:')
        for ingredient in ingredients:
            print(f'    {ingredient["ingredient_name"]}: {ingredient["quantity"]} {ingredient["measure"]}')
    for ingredient_name, quantity_and_measure in ingredient_for_cook.items():
        print(f'{ingredient_name}: {quantity_and_measure["quantity"]} {quantity_and_measure["measure"]}')


# Для соблюдения условия "не используем глобальные перменные" в атрибутах передаю книгу рецептов
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    ingredient_for_cook = {}
    for dish in cook_book.keys():
        if dish in dishes:
            for ingridients in cook_book[dish]:
                # вычисляет кол-во ингридиентов в зависимости от числа персон
                measure = ingridients['measure']
                quantity = ingridients['quantity'] * person_count
                # добавляем ингридиенты в новый словарь или прибавляем к ранее добавленному ингридиенту
                if not ingridients['ingredient_name'] in ingredient_for_cook.keys():
                    ingredient_for_cook[ingridients['ingredient_name']] = {'measure': measure, 'quantity': quantity}
                else:
                    ingredient_for_cook[ingridients['ingredient_name']]['quantity'] += quantity
    # возвращаем словарь ингридиентов
    return ingredient_for_cook


# Чтение книги рецептов в переменную.
def reading_cook_book(file_folder):
    file_cook_book = open(file_folder, 'rt')
    cook_book = {}
    dish_name = ''
    for line in file_cook_book:
        # Игнорируем числа, решил отказаться от числа
        if line.replace('\n', '').isdigit():
            continue
        # Фильтр по пустой строке, проверка на завершение списка ингридиентов.\
        # Подготовка к чтению нового блюда происходит путем очищение переменной dish.name
        elif not dish_name or not line.replace('\n', ''):
            dish_name = line.replace('\n', '')
            if dish_name:
                cook_book[dish_name] = []
        # Если создали новою блюдо, то заполняем список ингридиентов
        elif dish_name:
            ingredient, quantity, measure = line.replace('\n', '').split(' | ')
            cook_book[dish_name] += [{'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure}]
    file_cook_book.close()
    # Возвращаем заполненную кулинарную книгу
    return cook_book


main()
