shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order_set(menus, orders):
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order not in menus_set: # O(1)
            return False
    return True

def is_existing_target_order_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2

    return False

result = is_available_to_order_set(shop_menus, shop_orders)
print(result)
