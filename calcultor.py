print("Your calculator:")
num1 = int(input("enter num1="))
num2 = int(input("enter num2="))
print("available operators are +,-,*,**,/,//,%")
operator = input("enter operator:")

match operator:
    case '+':
        print("sum is",num1 + num2)
    case '-':
        print("difference is ",num1 - num2)
    case '*':
        print("product is", num1 * num2)
    case '/':
        print("division is", num1 / num2)
    case '%': 
        print("remainder is ", num1 % num2)
    case '**':
        print("power is", num1 ** num2)
    case '//':
        print("floor division is", num1 // num2)
    case '_':
        print("enter valid operator")
    