
#~ store multiple items / values in single variable
#~ items are ordered, changeable, allow duplicate
#~ items are indexed starting from 0

#> var_name = [1, 2, 1]

def contoh1():
    #~ List can contains items with different type
    my_list = [1, "Hello", True]
    print(f"{my_list = }")


def contoh2():
    #~ get list length using len() funtion
    my_list = [1, "Hello", True]
    my_list_length = len(my_list)
    print(f"{my_list_length = }")       # 3


def contoh3():
    #~ accessing list items using index
    my_list = [1, "Hello", True]
    print(f"{my_list[0] = }")       # 1


def contoh4():
    #~ my_list[START:END:STEP]
    my_list = [1, "Hello", True, 2, "Last"]
    print(f"{my_list[1:3] = }")     # ["Hello", True]


def contoh5():
    #~ change item at certain index
    my_list = [1, "Hello", True]
    my_list[1] = "Yami"
    print(f"{my_list = }")      # [1, "Yami", True]


def contoh6():
    #~ change items at certain range of index
    my_list = [1, "Hello", True, 2]
    print(f"Asal: {my_list = }")
    my_list[1:3] = ["Yami", False]
    print(f"Selepas Diubah: {my_list = }")      # [1, "Yami", False, 2]


def contoh7():
    #~ append item into list
    my_list = [1, "Hello", True]
    my_list.append("Extra")
    print(f"{my_list = }")      # [1, "Hello", True, "Extra"]


def contoh8():
    #~ insert item at certain index
    my_list = [1, "Hello", True]
    my_list.insert(1, "Extra")
    print(f"{my_list = }")      # [1, "Hello", "Extra", True]


def contoh9():
    #~ Reverse list
    my_list = [1, "Hello", True]
    my_list.reverse()
    print(f"{my_list = }")


def contoh10():
    #~ Clear List
    my_list = [1, "Hello", True]
    my_list.clear()
    print(f"{my_list = }")


def contoh11():
    #~ Take out item at certain index from the list
    my_list = [1, "Hello", True]
    x = my_list.pop(1)
    print(f"{my_list = }")
    print(f"{x = }")


if __name__ == "__main__":
    contoh11()
