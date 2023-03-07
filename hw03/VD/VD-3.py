# Interchange the values of two variables without using the third variable.
variable_1 = input("please enter value for variable_1: ")
variable_2 = input("please enter value for variable_2: ")
print("you have entered vriable_1", variable_1, "and variable_2", variable_2)
variable_1, variable_2 = variable_2, variable_1
print("after switching variable_1 is", variable_1, "and variable_2", variable_2)