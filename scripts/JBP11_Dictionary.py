#   store multiple items / values in single variable
#   items are unordered in Python 3.6 and earlier, changeable, no duplicate allowed
#   items are paired; key:value

#  Example:
# >    var_name = {"key1": "value1", "key2": "value2", "key3": "value3"}


def contoh1():
    # ~ How to create a dictionary and acces the value inside it
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    print(type(my_dict))
    print(my_dict["tarikh lahir"])


def contoh2():
    # ~ Access value from dictionary with possible non-existing key
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    print(my_dict.get("tarikh lahir"))


def contoh3():
    # ~ Check key x existenece
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    x = "tarikh lahir"
    if x in my_dict:
        print(f"Key {x} ada dalam my_dict!")
    else:
        print(f"Key {x} tiada dalam my_dict!")


def contoh4():
    # ~ Different way to loop through dictionary
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    print("Loop Key, Value")
    for key, value in my_dict.items():
        print(key, value)

    print("Loop key only")
    for key in my_dict:
        print(key)

    print("Loop value only")
    for key in my_dict:
        print(my_dict[key])

    print("Loop key only")
    for key in my_dict.keys():
        print(key)

    print("Loop value only")
    for value in my_dict.values():
        print(value)


def contoh5():
    # ~ Change the value of specific key
    # ? If given key does not exist yet, it will create new value instead

    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    print(my_dict)
    my_dict["umur"] = 27
    my_dict["nama"] = "Akarui"
    my_dict["tahun lahir"] = 1990 # add new item
    print(my_dict)


def contoh6():
    # ~ Change value using update method
    # ? If given key does not exist yet, it will create new value instead

    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    #new_data = [("umur", 27), ("hobi", "Coding")]
    new_data = {"umur": 27, "hobi": "Coding", "tahun lahir": 1990}
    print(my_dict)
    my_dict.update(new_data)
    print(my_dict)


def contoh7():
    # ~ Remove last item (3.7 >) | Remove random item (3.6 <)
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    x = my_dict.popitem()
    print(my_dict)
    print(x)


def contoh8():
    # ~ Remove item
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    x = my_dict.pop("umur")
    print(my_dict)
    print(x)


def contoh9():
    # ~ Clear dictionary
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    my_dict.clear()
    print(my_dict)


def contoh10():
    # ~ usesage of del keyword
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}
    del my_dict["hobi"]  # delete "hobi" item
    print(my_dict)
    del my_dict  # delete my_dict
    print(my_dict)


def contoh11():
    # ~ Copy dictionary
    my_dict = {"nama": "AkaruiYami Code", "umur": 17, "hobi": ["Main Game", "Coding"]}

    new_dict_1 = my_dict
    new_dict_2 = my_dict.copy()
    new_dict_3 = dict(my_dict)

    print_dict = lambda some_dict: print(f"{some_dict=}")

    print_dict(new_dict_1)
    print_dict(new_dict_2)
    print_dict(new_dict_3)

    my_dict["umur"] = 27

    print_dict(new_dict_1)
    print_dict(new_dict_2)
    print_dict(new_dict_3)


if __name__ == "__main__":
    contoh11()
