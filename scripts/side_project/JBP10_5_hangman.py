"""
Game hangman dalam terminal.

Pengguna akan teka huruf yang mungkin ada dalam perkataan misteri.
Sekiranya huruf yang pengguna teka itu ada, maka huruf tersebut akan di tunjukkan
dalam perkataan misteri tersebut.
Sekiranya huruf yang pengguna teka itu salah, maka cubaan penggunaan akan berkurang.
Pengguna akan tewas apabila semua cubaan sudah digunakan.

start:
    _ _ _ _ _   _ _ _

input:
    a

output:
    Betul!
    _ a _ a _   _ a _
"""
from random import choice

animal_list = (
    "ayam",
    "itik",
    "angsa",
    "katak",
    "kelawar",
    "lembu",
    "kerbau",
    "bangau",
    "burung kakak tua",
    "burung merpati",
    "ular sawa",
)

def print_board(word, letter_to_guess):
    for c in word:
        if c in letter_to_guess:
            print(" _ ", end="")
        else:
            print(f" {c} ".upper(), end="")
    print()

if __name__ == "__main__":
    random_word = choice(animal_list)
    letter_to_guess = set(random_word.replace(" ", ""))
    letter_guessed = set()
    n_trial = 3
    
    while True:
        print_board(random_word, letter_to_guess)
        guess = input("$  ").lower()

        if guess in letter_guessed:
            print(f"Huruf `{guess}` sudah di teka!")
            continue

        if guess in letter_to_guess:
            letter_to_guess.remove(guess)
            print("Betul!")
        else:
            n_trial -= 1
            if n_trial == 0:
                print("Anda sudah tewas!")
                break
            print(f"Salah! Anda hanya ada {n_trial} cubaan sahaja lagi.")

        if len(letter_to_guess) == 0:
            print("Anda sudah menang!")
            print(f"Perkataan Mister: {random_word.upper()}")
            break

        letter_guessed.add(guess)

