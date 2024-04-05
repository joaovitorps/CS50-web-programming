import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print(f"Only numbers allowed!")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print(f"Can't divide by zero!")
    sys.exit(1)
    
print(f"The result of the division btween {x} and {y} is {result}")