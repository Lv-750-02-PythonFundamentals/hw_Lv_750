"""3. Write a program to calculate the divide of two numbers entered by the user
sequentially through a comma, to predict the case of division by zero, cases of
syntactic errors and cases of other exceptional situations. Use the else and finally
blocks.
"""

lst = input("Plese enter several number using',': ").replace(" ", "").split(",")
print(lst)

def divide_prog(numb_1, numb_2):
    try:
        print(int(numb_1) / int(numb_2))
    
    except ZeroDivisionError as error:
        print(f"Error: {error} - numb_2 must be not 0")
    
    else:
        print("Isn't fun? :)")
    
    finally:
        print("Wanna try again?")

divide_prog(lst[0], lst[1])