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


def print_word(word_target, letter_guessed):
    for c in word_target:
        if c in letter_guessed or c == " ":
            print(c, end="")
        else:
            print("_", end="")
    print()


if __name__ == "__main__":
    print("Selamat Datang Ke Permainan Teka Kata!")
    print("\nAnda perlu meneka huruf yang mungkin ada dalam kata berikut.")
    print("Anda hanya mempunya 3 cubaan.")

    random_word = choice(animal_list)
    letter_to_guesse = set([c for c in random_word.replace(" ", "")])
    letter_guessed = set()
    n_trial = 3
    
    print(letter_to_guesse)
    while True:
        print_word(random_word, letter_guessed)
        guess = input("$  ").lower()

        if guess in letter_guessed:
            print(f"Huruf `{guess}` sudah diteka! Cuba huruf lain.")
            continue

        if guess in letter_to_guesse:
            letter_to_guesse.remove(guess)
            print("Betul!")
        else:
            n_trial -= 1
            print(f"Salah! Cubaan anda tinggal {n_trial} sahaja lagi.")

        if len(letter_to_guesse) == 0:
            print("Tahniah! Anda Menang!")
            print(random_word)
            break

        if n_trial == 0:
            print("Anda sudah tewas!")
            break

        letter_guessed.add(guess)