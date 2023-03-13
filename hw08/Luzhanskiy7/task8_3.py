from areas import area_of_triangle, area_of_rectangle, area_of_circle

print('1.Rectangle\n2.Tringle\n3.Circle')
choise = int(input('Select the area of what you want to calculate(enter 1,2,3):'))
if choise == 1:
    area_of_rectangle()
elif choise == 2:
    area_of_triangle()
elif choise == 3:
    area_of_circle()
else:
    print('Enter 1 or 2 or 3')
