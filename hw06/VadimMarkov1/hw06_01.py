def determine_numbers(n):
    even_numbers = []
    odd_numbers_div_3 = []
    numbers_not_div_2_3 = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even_numbers.append(i)
        elif i % 2 != 0 and i % 3 == 0:
            odd_numbers_div_3.append(i)
        else:
            numbers_not_div_2_3.append(i)
    return f"From numbers in the range from 1 to {n}:\n" \
           f"even numbers that are divisible by 2 - {' '.join(map(str, even_numbers))}\n" \
           f"odd numbers, which are divisible by 3 - {' '.join(map(str, odd_numbers_div_3))}\n" \
           f"numbers that are not divisible by 2 and 3 - {' '.join(map(str, numbers_not_div_2_3))}"


if __name__ == "__main__":
    print(determine_numbers(10))
