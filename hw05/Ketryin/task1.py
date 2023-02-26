# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function).

l= [1,2,3,4,5,6]
f=[]
for i in l:
    f.append(float(i))
print(f)