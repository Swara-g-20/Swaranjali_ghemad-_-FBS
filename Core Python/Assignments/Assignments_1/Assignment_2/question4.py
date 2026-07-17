##WAP to calculate area of triangle and rectangle
triangle_base = float(input("Enter base of triangle: "))
triangle_height = float(input("Enter height of triangle: "))
rectangle_length = float(input("Enter length of rectangle: "))
rectangle_width = float(input("Enter width of rectangle: "))

triangle_area = 0.5 * triangle_base * triangle_height
rectangle_area = rectangle_length * rectangle_width

print("Area of triangle:", triangle_area)
print("Area of rectangle:", rectangle_area)