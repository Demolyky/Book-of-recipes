file_cook_book = open('Cookbook.txt', 'rt')
cook_book = {}
dish_name = ''
for line in file_cook_book:
    if line.replace('\n', '').isdigit():
        continue
    elif not dish_name or not line.replace('\n', ''):
        dish_name = line.replace('\n', '')
        if dish_name:
            cook_book[dish_name] = []
    elif dish_name:
        ingredient, quantity, measure = line.replace('\n', '').split(' | ')
        cook_book[dish_name] += [{'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure}]
        
print(cook_book)
file_cook_book.close()