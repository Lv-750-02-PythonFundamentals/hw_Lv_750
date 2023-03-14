'''Якщо ми перерахуємо всі натуральні числа нижче 10, кратні 3 або 5, то отримаємо 3, 5, 6 і 9.
Сума цих кратних дорівнює 23.

Примітка. Якщо число кратне 3 і 5, порахуйте його лише один раз.
'''

def solution(number):
    numbers = []
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            numbers.append(n)
    return sum(numbers)

solution(10)
