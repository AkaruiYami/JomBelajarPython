from datetime import date

tahun_lahir = int(input("Masukkan Tahun Kelahiran Anda: "))
umur = date.today().year - tahun_lahir

if umur > 18:
    print("Umur anda sudah melebihi 18 tahun")
elif umur == 18:
    print("Umur anda adalah 18 tahun")
else:
    print("Umur anda belum capai 18 tahun")


print()
# Kalau umur 18 tahun dan ke atas, status = B
# Kalau umur bawah 18 tahun, status = A
# Printkan status

status = 'A' if umur < 18 else 'B'
print(f"Status = {status}")


print()
# Semak sama ada nilai yang diberikan oleh user adalah titik tengah
# yang berada antara nilai_bawah dan nilai_atas
nilai_bawah = 5
nilai_atas = 12
nilai_user = int(input("Masukkan Sebarang Nilai: "))

if nilai_user >= nilai_bawah and nilai_user <= nilai_atas:
    print(f"{nilai_user} berada dalam jarak")
else:
    print(f"{nilai_user} berada di luar jarak")


print()
pelajar_a = {
    "nama": "AkaruiYami Code",
    "umur": 17, # tehe
    "hobi": ["Coding", "Main Game"],
    "id": "idk_apa_idk"
}

if pelajar_a["umur"] < 18:
    if "Coding" in pelajar_a["hobi"]:
        print("Pelajar ni masih bawah 18 tahun dan suka coding.")

        bahasa_komputer = input("Programing Language apa yang ko selalu guna: ")
        if bahasa_komputer.lower() == "python":
            print("Ularkah itu?")
        elif bahasa_komputer.lower() == "c++":
            print("Banyak tambah nya tu.")
        elif bahasa_komputer.lower() == "java":
            print("Kedua")
        else:
            print("K")
    
    if "Main Game" in pelajar_a["hobi"]:
        print("Suka beno main game nyer. Study jangan lupa.")

    if "Baca Buku" in pelajar_a["hobi"]:
        print("Bagus, bagus. Buku apa yang kau baca tu?")
else:
    print("Ok, dah 18 ke atas.")


