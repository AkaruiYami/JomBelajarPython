while True:
    for y in range(5):
        for x in range(5):
            print(f" {x}{y} ", end='')
        print()
    
    # minta input daripada user
    # keluar daripada loop jika input adalah N ataupun n
    ulang = input("Ulang semula [Y / N]: ")
    if ulang == 'N' or ulang == 'n':
        break


# go through sequance of number from 2 until 9
for n in range(2, 10):
    print(n)
else:
    print("Sudah siap menyalin elemen dalam jujutan nombor.")


# go through each element inside list
buah_tempatan = ["durian", "rambutan", "manggis", "betik"]
for buah in buah_tempatan:
    print(buah)
else:
    print("Semuah buah sudah di semak.")


# go through each character inside the string
nama = "AkaruiYami Code"
for huruf in nama:
    # sekirannya huruf tersebut adalah ruang kosong (space), jangan print (skip)
    if huruf == " ":
        continue
    print(huruf)