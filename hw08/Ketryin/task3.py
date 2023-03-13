import task3_function
print("Choose the figure: ")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

figure = input("Enter number of figure: ")
if figure == '1':
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f'Area of rectangle:{task3_function.area_rectangle(length, width)}')
    
if figure == '2':
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    print(f'Area of triangle:{task3_function.area_triangle(base, height)}')

if figure == '3':
    r = int(input("Enter radius: "))
    print(f'Area of circle:{task3_function.area_circle(r)}')