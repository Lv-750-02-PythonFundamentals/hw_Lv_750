n = input("Enter a list of numbers, separate the numbers with a space: ").split()
result = []

for num in n: result.append(int(num))

print(f"Еhe maximum number from the list: {max(result)};\n"
      f"The minimum number from the list: {min(result)}.")