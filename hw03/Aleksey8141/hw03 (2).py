'''A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number
3. Interchange the values of two variables without using the third variable.'''

# a = int(input())
# prod = 1
# while a!=0:
#     n = a%10
#     prod = prod*n
#     a = a//10
# print(prod)

a = int(input())
a1 = str(a)
b = list(a1)
b.reverse()
b = "".join(b)
b1 = [int(i) for i in a1]



prod = 1
n4 = a%10
prod = prod*n4
a = a//10

n3 = a%10
prod = prod*n3
a = a//10

n2 = a%10
prod = prod*n2
a = a//10

n1 = a%10
prod = prod*n1
a = a//10
print('Добуток цифр =', n1*n2*n3*n4)
print('У зворотньому порядку число =', b)
print('Відсортовані числа =', sorted(b1))
