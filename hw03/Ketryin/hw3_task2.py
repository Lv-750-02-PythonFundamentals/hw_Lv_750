number = int(input("Input  four-digit number: "))

n, d = divmod(number, 10)
n, c = divmod(n, 10)
a, b = divmod(n, 10)

print(a*b*c*d)

print(d*1000 + c*100 + b*10 + a)

list = [a, b, c, d]
list.sort()
print(list)