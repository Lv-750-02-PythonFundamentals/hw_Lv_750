number = int(input('Enter a number:'))
fibo = [0, 1]
for i in range(number + 1):
    fibo.append(fibo[-2] + fibo[-1])
print(fibo)
