def sambut():
    print("Selamat Datang.")
    print("AkaruiYami Code")

sambut()


def tambah(a, b):
    return a + b

print(tambah(1, 2))


def menaik(x, langkah=2):
    return x + langkah
print(menaik(1))

# menaik = lambda a, langkah: a + langkah
# print(menaik(1, 10))


def fungsi3(a, b, c=0, d=0):
    print(f"A: {a}, B: {b}, C: {c}, D:{d}")

fungsi3(1, 2, d=10)


def fungsi1(a, *args):
    print(f"A: {a}, ARGS: {args}")

fungsi1(1, 2, 3, 4, 5)


def fungsi2(a, **kwargs):
    print(kwargs)

fungsi2("A", nama="AkaruiYami", umur=17)


def return_multiple_value(a, b):
    return a, b

x, y = return_multiple_value(1, "Yami")
print(y)


def main():
    pass


def recursion_func(a, n):
    print(a+n)
    n -= 1
    if n > 0:
        recursion_func(a, n)

recursion_func(10, 7)


jumlah = lambda a, b: (a, b)
tmp = jumlah(1, 5)
print(tmp)

