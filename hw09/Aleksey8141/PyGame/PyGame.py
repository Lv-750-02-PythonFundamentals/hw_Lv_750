'''
Сценарій гри "Вгадай число":

Початок гри:

Програма генерує випадкове число з діапазону 1-100 і зберігає його у змінній "secret_number".
Програма виводить привітальне повідомлення з правилами гри: "Привіт! Я задумав число від 1 до 100.
У вас є 10 спроб, щоб вгадати його.
Після кожної спроби я скажу, чи загадане число більше чи менше введеного вами числа. Почнемо гру!"
Гравець вводить свою першу спробу:

Програма зчитує введене користувачем число і зберігає його у змінній "guess".
Програма перевіряє, чи вгадане число дорівнює "secret_number":
Якщо "guess" дорівнює "secret_number", програма виводить повідомлення про перемогу:
"Вітаю! Ви виграли! Загадане число дійсно було {secret_number}!"
Якщо "guess" не дорівнює "secret_number", програма переходить до наступного кроку.
Гравець має ще 9 спроб:

Програма виводить повідомлення, яке повідомляє гравцю, чи "secret_number" більше чи менше від "guess":
"Моє число {менше/більше} за {guess}. Спробуйте ще раз!".
Програма запитує гравця ввести наступну спробу.
Програма повторює кроки 2-3 ще 8 разів.
Гравець використав усі 10 спроб:

Програма виводить повідомлення про програш: "На жаль, ви не вгадали число за 10 спроб.
Загадане число було {secret_number}. Спробуйте ще раз!"
Кінець гри.
'''

import random

secret_number = random.randint(1, 100)
attempts = 10

print("Привіт! Я задумав число від 1 до 100. У вас є 10 спроб, щоб вгадати його. Після кожної спроби я скажу, чи загадане число більше чи менше введеного вами числа. Почнемо гру!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба #{attempt}: "))
    if guess == secret_number:
        print(f"Вітаю! Ви виграли! Загадане число дійсно було {secret_number}!")
        break
    elif guess < secret_number:
        print("Моє число більше за", guess)
    else:
        print("Моє число менше за", guess)

    if attempt == attempts:
        print(f"На жаль, ви не вгадали число за {attempts} спроб. Загадане число було {secret_number}. Спробуйте ще раз!")

