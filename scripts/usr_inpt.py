from datetime import date

nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))

tahun_semasa = int(date.today().year)

print(f'{nama} lahir pada tahun {tahun_semasa - umur}')

