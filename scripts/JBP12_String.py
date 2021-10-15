def contoh1():
    # ~ Can either use sigle quote or double quote
    str1 = "Hello"
    str2 = "Hello"

    print(type(str1))
    print(type(str2))


def contoh2():
    # ~ Use 3 single/double quotes to create multiline string
    str1 = """Ini adalah contoh multiline string.
    Ini adalah line 2.
    Ini pula line 3."""

    print(str1)


def contoh3(str1="abcdefg"):
    # ~  Acces character in string
    print(str1[1])  # should print 'b'


def contoh4(str1="AkaruiYami"):
    # ~ Loop through string
    for c in str1:
        print(c)


def contoh5(str1="AkaruiYami"):
    # ~ Get the number of character inside the string
    n = len(str1)
    print(n)


def contoh6(str1="AkaruiYami"):
    # ~ Checking word/character inside string
    if "Akarui" in str1:
        print("Akarui is inside str1.")

    if "Code" not in str1:
        print("Code is not in str1")


def contoh7():
    # ~ String formating
    name = "AkaruiYami"
    age = 17

    greeting = "My name is {} and I am {} years old"
    print(greeting.format(name, age))

    fstring_greeting = f"My name is {name} and I am {age} years old"
    print(fstring_greeting)


def contoh8(
    str1=" AkaruiYami|Code ", to_replace=("a", "5"), to_split="|", to_strip=None
):
    # ~ Modify string
    str1_upper = str1.upper()
    str1_lower = str1.lower()
    str1_replace = str1.replace(to_replace[0], to_replace[1])
    str1_split = str1.split(to_split)
    str1_strip = str1.strip(to_strip)

    print(f"{str1_upper=}")
    print(f"{str1_lower=}")
    print(f"{str1_replace=}")
    print(f"{str1_split=}")
    print(f"{str1_strip=}")


def contoh9():
    # Combine string
    str1 = "Akarui"
    str2 = "Code"

    print(str1 + " " + str2)


def contoh10():
    str1 = "My name is \"AkaruiYami\""
    str2 = 'My name is "AkaruiYami".'

    print(str1)
    print(str2)


if __name__ == "__main__":
    pass
