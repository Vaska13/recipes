import os

def read_recipes_from_file(filename):
    """Читает рецепты из файла и возвращает словарь cook_book."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    cook_book = {}
    index = 0

    while index < len(lines):
        dish_name = lines[index]
        index += 1

        if index >= len(lines):
            raise ValueError("Файл повреждён: ожидается количество ингредиентов после названия блюда")

        try:
            ingredients_count = int(lines[index])
        except ValueError:
            raise ValueError(f"Ошибка формата файла: следующая строка должна быть числом (количество ингредиентов): '{lines[index]}'")
        except IndexError:
            raise ValueError("Файл повреждён: неожиданный конец файла при чтении количества ингредиентов")

        index += 1

        ingredients = []
        for _ in range(ingredients_count):
            if index >= len(lines):
                raise ValueError("Файл повреждён или неполный")
            ingredient_data = lines[index].split(' | ')
            if len(ingredient_data) != 3:
                raise ValueError(f"Ошибка формата строки ингредиента: {lines[index]}")

            name, quantity_str, measure = ingredient_data
            try:
                quantity = int(quantity_str)
            except ValueError:
                raise ValueError(f"Количество должно быть числом: {quantity_str}")

            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
            index += 1

        cook_book[dish_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    """Возвращает словарь с ингредиентами и их количеством для заданных блюд на указанное число персон."""
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            raise ValueError(f"Блюдо '{dish}' не найдено в кулинарной книге")

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list


def main():
    # Получаем путь к текущей директории
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, 'files', 'recipes.txt')

    try:
        # Чтение рецептов
        cook_book = read_recipes_from_file(filename)

        # Пример вызова функции
        dishes = ['Запеченный картофель', 'Омлет']
        person_count = 2
        shopping_list = get_shop_list_by_dishes(cook_book, dishes, person_count)

        # Вывод результата
        print("Список покупок:")
        for ingredient, data in shopping_list.items():
            print(f"{ingredient}: {data['quantity']} {data['measure']}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()