user_number = int(input("Enter your number: "))

first_value = 0
second_value = 1

for i in range(0, user_number):
    if i <= 1:
        next_value = i
    else:
        next_value = first_value + second_value
        first_value = second_value
        second_value = next_value
    print(next_value)
