'''Create a list that contains elements of integer type, then
use the loop to change the type of these elements to a floating
type.
(Hint: use the built-in float () function)'''

int_list = [2, 4, 6, 7, 8, 10]
counter = 0
for i in int_list:
        counter += 1
        int_list.append(float(i))
        print(float(i))
        if counter == 6:
            break



