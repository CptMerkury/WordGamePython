import random

words_bank = [
    'автострада', 'бензин', 'инопланетянин', 'самолет',
    'библиотека', 'шайба', 'олимпиада'
]

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)

print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('Write one russian letter: ').lower()
    if len(letter) != 1:
        continue
    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('You won')
    else:
        errors_counter += 1
        print('Wrong answer', errors_counter)
        if errors_counter == 8:
            print('You lose; (')
            break
    print(''.join(gamer_word))
