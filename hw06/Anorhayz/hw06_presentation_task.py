user_numbers = input("Enter your number, use 'space' to separate them: ").split()
user_list = []

for element in user_numbers:
    user_list.append(int(element))

print(f"Maximum number is: {max(user_list)}")
print(f"Minimum number is: {min(user_list)}")
