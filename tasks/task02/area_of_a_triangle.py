import math


def get_triangle_calc_variable(title):
    result = []
    for item in input(f'\n[{title}]: ').split(' '):
        result.append(int(item))
    return result


def calculate_triangle_by_base_height(variables):
    return (variables[0]*variables[1])/2


MENU_LIST_ROOT = [
    {
        'title': 'Calculate triangle area by base and height',
        'action': calculate_triangle_by_base_height
    },
    {
        'title': 'Calculate triangle area by 2 sides and angle between them',
        'action': lambda variables:  calculate_triangle_by_base_height(variables)*math.sin(math.radians(variables[2]))
    }
]


def print_menu_items(items):
    print('\n\n')
    index = 1
    for item in items:
        print(f"{index}. {item['title']}")
        index += 1
    print('0. Exit')


def execute_menu_action(item):
    if 'action' in item:
        title = item["title"]
        action = item['action']
        area_value = action(get_triangle_calc_variable(title))
        input(f'Area is: {area_value}.\nFor return enter any key')


def menu_controller(menu_item, index):
    if index == -1:
        return False

    if index > -1:
        execute_menu_action(menu_item[index])

    return True


def select_menu_item_index(items):
    selected_item = input('Please, select menu item: ')
    length = len(items)
    index = int(selected_item) if selected_item.isnumeric() else length
    if index == 0:
        return -1
    elif index <= length:
        return index-1
    return -2


def menu_loop(menu_items):
    is_running = True
    while is_running:
        print_menu_items(menu_items)
        is_running = menu_controller(menu_items, select_menu_item_index(menu_items))


menu_loop(MENU_LIST_ROOT)
