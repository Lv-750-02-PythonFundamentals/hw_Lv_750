even_div_by_2 = []
odd_div_by_3 = []
not_div_by_2_or_3 = []

for i in range(1, 10):
    if i % 2 == 0:
        even_div_by_2.append(i)
    elif i % 3 == 0 and i % 2 == 1:
        odd_div_by_3.append(i)

# я тут написав >, а не ==, так як при операторі == в список не попадає пʼятірка, яка за умовами до нього підходить, тому що
# не ділиться ні на 2, ні на 3
    elif i % 2 > 0 and i % 3 > 0:
        not_div_by_2_or_3.append(i)
print(even_div_by_2, odd_div_by_3, not_div_by_2_or_3)
