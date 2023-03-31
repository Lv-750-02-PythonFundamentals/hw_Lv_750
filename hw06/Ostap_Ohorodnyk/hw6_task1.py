number_for_range = int(input("Enter number from 1 to 10: "))
even_number = []
add_number_divisible_by_3 = []
rest_number = []

for number in range(1,number_for_range+1):
    if number % 2 ==0:
        even_number.append(number)
    elif number % 3 == 0:
        add_number_divisible_by_3.append(number)
    else:
        rest_number.append(number)

print(f'Even number: {even_number};\nOdd numbers, which are divisible by 3 :{add_number_divisible_by_3};\n'
      f'Number that are not divisible by 2 and 3 :{rest_number}')
