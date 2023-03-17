import random as rnd

random_value = rnd.randint(1, 100)
i = 0
print("Guess a number between 1 and 100. You have 10 tries.")
while i <= 10:
    i += 1
    val = int(input())
    if val == random_value:
        print("Congratulations. So. This is the correct answer.")
        break

    if val < random_value:
        print("Your value is less than the specified value")
    else:
        print("Your value is greater than the given value")

print("No more attempts, try again next time.")