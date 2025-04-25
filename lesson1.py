vowels = "AEIOUАЕЁИОУЫЭЮЯ"
consonants = "BCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

while True:
    word = input("Слово (или 'exit' для выхода): ").upper()

    if word == "EXIT":
        print("Программа завершена")
        break

    count_letters = 0
    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter.isalpha():
            count_letters += 1

            if letter in vowels:
                vowel_count += 1
            elif letter in consonants:
                consonant_count += 1

    print(f"\nСлово: {word}")
    print(f"Всего букв: {count_letters}")
    print(f"Гласных: {vowel_count}")
    print(f"Согласных: {consonant_count}")

    if count_letters > 0:
        vowels_percent = (vowel_count / count_letters) * 100
        consonants_percent = (consonant_count / count_letters) * 100

        print(f"Гласные: {vowels_percent:.2f}%")
        print(f"Согласные: {consonants_percent:.2f}%\n")
    else:
        print("В слове нет букв!\n")