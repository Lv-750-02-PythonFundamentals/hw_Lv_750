firs_variable = input("Enter your first variable: ")
second_variable = input("Enter your second variable: ")

print("firs variable = " + firs_variable,"\n""second variable = " + second_variable,'\n')

firs_variable, second_variable = second_variable, firs_variable

print(f"Value after exchanging the values of the two variables :"
      f"\nfirs variable = {firs_variable}\nsecond variable = {second_variable}")