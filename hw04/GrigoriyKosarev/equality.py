"""
Write a script, which of the two entered
numbers will determine which of them is
more and which is less. Take into account
the case of equality of numbers
"""
print("a= ")
a = int(input())
print("b= ")
b = int(input())

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")