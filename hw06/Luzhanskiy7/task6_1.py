numbers, even, odd, even_odd = [], [], [], []

for i in range(1, 11):
    numbers.append(i)
print('numbers from 1 to 10: ', numbers)
for j in numbers:
    if j % 2 == 0:
        even.append(j)
    elif j % 2 != 0 and j % 3 == 0:
        odd.append(j)
    elif j % 2 != 0 and j % 3 != 0:
        even_odd.append(j)
print('even numbers that are divisible by 2:', even)
print('odd numbers which are divisible by 3:', odd)
print('numbers that are not divisible by 2 and 3:', even_odd)