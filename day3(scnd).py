'''Program to Calculate the Area of a Circle and Triangle:
Write a program to calculate the area of a circle given its radius and a triangle given its base and height.'''




radius = float(input("Enter the radius of the circle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
circle_area = 3.14159 * radius * radius  
print("Area of the circle is:", circle_area)
triangle_area = 0.5 * base * height 
print("Area of the triangle is:", triangle_area)


'''Output:
Enter the radius of the circle: 5
Enter the base of the triangle: 10
Enter the height of the triangle: 8
Area of the circle is: 78.53975
Area of the triangle is: 40.0'''