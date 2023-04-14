"""With help input obtain from user his age. Age must be natural number.

If user try input incorrect value ask him again. If user typed correct age print this value.

Do not use if in your code, but you can use already created function check_age for validation.
"""

#You can edit code below
ask = 1

while ask:
    try:
        age = int(input())
        check_age(age)
        ask = 0
    except ValueError:
        pass
    else:
        print(age)



