user_number = input("Please enter your four-digit number: ")
print(f"Your number is: {user_number}")

product_number = int(user_number)


def getProduct(n):
    product = 1

    while n != 0:
        product = product * (n % 10)
        n = n // 10

    return product


print(getProduct(product_number))

print(str(user_number)[::-1])
print(sorted(user_number))
