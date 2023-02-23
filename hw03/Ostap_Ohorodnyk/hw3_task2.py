four_gigits_number = input("plese enter four-digits number: ")
produkt_of_numbers = int(four_gigits_number[0]) * int(four_gigits_number[1]) \
                     * int(four_gigits_number[2]) * int(four_gigits_number[3])

list_of_digits = list(four_gigits_number)

reverse_digits = list_of_digits[::-1]

sorted_number = sorted(list_of_digits)

print(f"Product of the numbers is: {produkt_of_numbers}\nNumbers in reverse order: {''.join(reverse_digits)}\n\
Numbers sorted in ascending order: {''.join(sorted_number)}")