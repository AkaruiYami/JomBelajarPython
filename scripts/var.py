
nama = str('AkaruiYami Code')
umur = int(17)
hobi = ['Coding', 'Main Game']

print(nama)
print(umur)
print(hobi)

nama = ['AkaruiYami', 'Code']
umur = str(umur)
hobi = 2

print(nama)
print(umur)
print(hobi)


def func1():
    global nama
    nama = 'Kamu'
    print(nama)

func1()
print(nama)