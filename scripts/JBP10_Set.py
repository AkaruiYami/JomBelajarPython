# ~ store multiple items / values in single variable
# ~ items are unordered, unchangeable, no duplicate allowed
# ~ items are unindexed

# Example:
#     var_name = {1, 2, 3}


def contoh1():
    # ~ Loop through set
    set_a = {"Durian", "Rambutan", "Manggis"}
    for buah in set_a:
        print(buah)


def contoh2():
    # ~ Check if item exist in set
    set_a = {"Durian", "Rambutan", "Manggis"}
    print("Durian" in set_a)


def contoh3():
    # ~ Add single item into existing set
    set_a = {"Durian", "Rambutan", "Manggis"}
    print(set_a)

    set_a.add("Ciku")
    print(set_a)


def contoh4():
    # ~ Add item into existing set from iterable
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_b = {"Strawberi", "Anggur", "Epel"}
    list_a = ["Mangga", "Betik"]
    set_a.update(list_a)

    print(set_a)


def contoh5():
    # ~ Remove item from set. Will Raise error if item does not exist
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_a.remove("Epel")
    print(set_a)


def contoh6():
    # ~ Remove item from set without raising error
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_a.discard("Epel")
    print(set_a)


def contoh7():
    # ~ Clear set
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_a.clear()
    print(set_a)
    # ~ Delete set
    del set_a


def contoh8():
    # ~ Create new set that contain all item from 2 set
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_b = {1, 2, 3}
    set_c = set_a.union(set_b)
    print(set_c)


def contoh9():
    # ~ Create new set that contain all item EXCEPT the non duplicate item from 2 set
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_b = {"Mangga", "Durian"}

    set_z = set_a.intersection(set_b)
    set_a.intersection_update(set_b)
    print(set_a)
    print(set_z)


def contoh10():
    # ~ Create new set that contain all item EXCEPT the duplicate item from 2 set
    set_a = {"Durian", "Rambutan", "Manggis"}
    set_b = {"Mangga", "Durian"}

    set_z = set_a.symmetric_difference(set_b)
    set_a.symmetric_difference_update(set_b)
    print(set_a)


if __name__ == "__main__":
    contoh10()
