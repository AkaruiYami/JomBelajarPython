# ~ store multiple items / values in single variable
# ~ items are ordered, unchangeable, allow duplicate
# ~ items are indexed starting from 0

# > var_name = (1, 2, 2, 3)


def contoh1():
    # Create Tuple with 1 value
    tupl = ("Value 1",)
    print(type(tupl))


def contoh2():
    # ~ Tuple can have value with different data type
    tupl = (1, True, "Last Value")
    print(tupl)


def contoh3():
    # ~ Check Tuple lenght using len() function
    tupl = (1, True, "last Value")
    print(len(tupl))


def contoh4():
    # ~ Assessing item using index
    tupl = (1, True, "last Value", "Extra Value", 114)
    target = tupl[2:4]
    print(target)


def contoh5():
    # ~ Update Tuple Value
    #! Tuple cannot be change on created, but there is a work around
    tupl = (1, True, "last Value")
    tupl = list(tupl)
    tupl[1] = False
    tupl = tuple(tupl)
    print(tupl)


def contoh6():
    # ~ Add item in tuple
    #! Tuple are immutable / unchangeable, but there is a work around
    a = (1, True, "last Value")
    a = list(a)
    a.append("Extra Value")
    a = tuple(a)
    print(a)


def contoh7():
    # ~ Unpack tuple
    tupl = (1, True, "last Value")
    a, b, c = tupl
    print(f"{a=}, {b=}, {c=}")


def contoh8():
    # ~ More on unpack tuple
    tupl = (1, 0, 0, 1, 1, 2, 3, 4, 5)
    x, y, *z, k = tupl
    print(f"{x=}, {y=}, {z=}, {k=}")


def contoh9():
    # ~ Loop tuple
    tupl = (1, True, "last Value")
    for i, item in enumerate(tupl):
        print(i, item)


def contoh10():
    # ~ Join tuples
    tupl1 = ("Value1", "Value2")
    tupl2 = ("ValueA", "ValueB")
    tupl3 = ("Value@", "Value$")
    joined_tupl = tupl1 + tupl2 + tupl3
    print(joined_tupl)


def contoh11():
    # ~ Tuple Method
    tupl = (1, 1, "last Value", "True", "True")
    print(tupl.count(True))
    print(tupl.index("True"))


if __name__ == "__main__":
    pass
