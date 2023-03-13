num = input("Enter your 4-digit number: ")
digits = list(num)
digits2 = list(num)

product = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])

digits.reverse()
digits2.sort()

print(f"Product of the numbers is: {product}\nNumbers in reverse order: {digits}\n\
Numbers sorted in ascending order: {digits2}")