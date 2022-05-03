from objects_rectangle import * 
from random import randint


rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19))
)

print("rectangle coordinates:",
    rectangle.lowleft.x, ",",
    rectangle.lowleft.y, "and",
    rectangle.upright.x, ",",
    rectangle.upright.y

)

user_point = print(
    float(input("Guess rectangle area X:")),
    float(input("Guess rectangle area Y:"))
)

print("Your point was inside rectangle: ",
        user_point.rectangle(rectangle))

print("Your Area was off by: ", rectangle.area() - user_area )