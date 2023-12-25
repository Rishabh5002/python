#exception handling
a = int(input("enter a"))
b = int(input("enter b"))

try: 
    result = a / b
except ZeroDivisionError:
    result = None
    print("Can not divide by 0")
finally:
    print("division operation completed:", result)