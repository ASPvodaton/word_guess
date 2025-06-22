import random
word_list = [
    "предисловие", "глава", "обзор", "тематика", "курс", "последствия", "невежество",
    "жизнь", "личность", "общество", "область", "социология", "отрасль", "состоятельность",
    "наука", "несостоятельность", "теория", "измерение", "оценка", "исследователь",
    "источник", "знание", "ошибка", "свобода", "исследование", "ограничение", "информация",
    "характер", "задача"
]
    
def get_word(word_list):
    return random.choice(word_list) 

def display_hangman(tries):
    stages = [
        # tries = 0
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
        # tries = 1
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |
        """,
        # tries = 2
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        """,
        # tries = 3
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |
        """,
        # tries = 4
        """
           --------
           |      |
           |      O
           |      |
           |      
           |
        """,
        # tries = 5
        """
           --------
           |      |
           |      O
           |    
           |      
           |
        """,
        # tries = 6 (начальная пустая виселица)
        """
           --------
           |      |
           |      
           |    
           |      
           |
        """
    ]
    return stages[tries]

def play(word):
    word = word.upper()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        print('слово состоит из ', len(word), ' букв!')
        guess = input("Введите букву или слово целиком: ").upper()

        # Защита от ввода недопустимых символов
        if not guess.isalpha():
            print("Ошибка: нужно ввести только буквы.")
            continue

        # Один символ — попытка угадать букву
        if len(guess) == 1:
            if guess in guessed_letters:
                print(f"Вы уже называли букву {guess}.")
            elif guess in word:
                guessed_letters.append(guess)
                print(f"Угадали! Буква {guess} есть в слове.")
                # Обновляем строку с подчёркиваниями
                word_completion = "".join([
                    letter if letter in guessed_letters else "_"
                    for letter in word
                ])
                if "_" not in word_completion:
                    guessed = True
            else:
                print(f"Буквы {guess} нет в слове.")
                tries -= 1
                guessed_letters.append(guess)

        # Если пользователь вводит всё слово
        else:
            if guess in guessed_words:
                print(f"Слово {guess} уже называлось.")
            elif guess == word:
                guessed = True
                word_completion = word
            else:
                print(f"{guess} — неверное слово.")
                tries -= 1
                guessed_words.append(guess)

        print(display_hangman(tries))
        print(word_completion)
        
        print()

    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    else:
        print(f"Увы, вы проиграли. Загаданное слово было: {word}")
def main():
    while True:
        word = get_word(word_list)
        play(word)

        again = input("Сыграем ещё раз? (да/нет): ").strip().lower()
        if again not in ('да', 'д', 'yes', 'y'):
            print("Спасибо за игру!")
            break
main()
