import sys

def find_duplicates(args):
    seen = set()
    duplicates = set()

    for arg in args:
        if arg in seen:
            duplicates.add(arg)
        else:
            seen.add(arg)
    return list(duplicates)

def ft_find_max(inventory_dict: dict) -> None:
    filtered_abundance = {}
    for name, quantity in inventory_dict.items():
        max = 1
        if quantity > max:
            max = quantity
    filtered_abundance.update({name: quantity})
    if filtered_abundance:
        print(f"Item most abundant: {filtered_abundance} with quantity {inventory_dict}")

def ft_find_min(inventory_dict: dict) -> None:
    filtered_abundance = {}
    for name, quantity in inventory_dict.items():
        min = 1
        if quantity < min:
            min = quantity
    filtered_abundance.update({name: quantity})
    if filtered_abundance:
        print(f"Item most abundant: {filtered_abundance} with quantity {inventory_dict}")

def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory_dict = {}
    i = 1
    while i < len(sys.argv):
        input = sys.argv[i]
        item = sys.argv[i].split(":")
        name = item[0]
        quantity = int(item[1])
        inventory_dict.update({name: quantity}) 
        # try:
        #     if len(item) != 2 or not item[0] or not item[1]:
        #         print("Error")
        # except ValueError:
        #     print(f"Error invalid parameter {sys.argv[i]}")
        i += 1

    my_keys = list(inventory_dict)
    
    dupes = find_duplicates(sys.argv[1:])
    print(f"Redundant items '{dupes}' - discarding")
    print(f"Got inventory: {inventory_dict}")
    print(f"Item list: {inventory_dict.keys()}")
    print(f"Total quantity of {len(inventory_dict)} items: {sum(inventory_dict.values())}")
    j = 0
    while j != len(inventory_dict.keys()):
        print(f"Item {my_keys[j]} {inventory_dict[(my_keys[j])]/sum(inventory_dict.values()):.1%}")
        j += 1
    #print(f"Item most abundant: {inventory_dict.keys()} with quantity {inventory_dict.values}")
    ft_find_max(inventory_dict)
    ft_find_min(inventory_dict)
    inventory_dict['magic_item'] = 1
    print(f"Updates inventory: {inventory_dict}")


if __name__ == "__main__":
    ft_inventory_system()


    # for key in inventory_dict:
    #     inventory_dict['sys.argv[i]'] = 
    #    inputs = sys.argv[1:]
    # if len(inputs) != len(set(inputs)):
    #     print("redudent item '{}'")

    # #Gets inputs and count frequency
    # inputs = sys.argv[1:]
    # counts = Counter(inputs)

    # #GCreate a list of duplicates 
    # duplicates = [item for item, count in counts.items() if count > 1]

    # if duplicates:
    #     print(f"redudent item '{', '.join(duplicates)}")