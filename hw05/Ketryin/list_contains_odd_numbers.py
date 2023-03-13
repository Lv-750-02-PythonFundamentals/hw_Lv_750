# Check if the list contains odd numbers.
# (Hint: use the break statement)

l= [1,2,3,4,5,6]
f=[2,4,6,8,10]

def list_contains_odd_numbers(list_numbers):
    for i in list_numbers:
        if i%2==1:
            print('list contains odd numbers')
            break
    else:
        print('list does not contains odd numbers')

list_contains_odd_numbers(l)
list_contains_odd_numbers(f)