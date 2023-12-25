def outer_function():
    x = 1 

    def inner_function():
        y = 2
        result  = x + y
        return result
    
    return inner_function()
output = outer_function()
print(output)

def add(x):
    x = x+1
    print("inner function:", x)
x = 5
add(x)
print("outer function:", x)


#pass by reference
def modify_list(list):
    list.append(4)
    list = [4,5,6]
    print("inside functiom:", list)

list = [1,2,3]
modify_list(list)
print("outside function:", list)


#ques
def factorial():
    if n== 0:
     ans = 1
    else: 
       for i in range(1, n+1):
          ans *= i
    return ans

n = int(input("emter number:"))
output = factorial()
print("factorial of number is", output)


def factorial (n):
    #base case 
    if n == 0:
        return 1
    
     #recursive case 
    ans = n*factorial(n-1)
    return ans

n = int(input("enter a number:"))
print(factorial(n)) 


#ques
def numbers(n):
    #base case
    if n==0:
      return
    #recursive case
    numbers(n-1)
    print(n)

n = int(input("enter a number"))
print(numbers(n))

#ques
def numbers(n):
   if n==0:
      return
   else:
      for i in range(1,n):
         print(i)
n = int(input("emter a number"))
print(numbers(n))

#ques
def sumofnumbers(n):
    if n == 1:
     return 1
    ans = n + sumofnumbers(n-1)
    return ans
    
n = int(input("enter number:"))
print(sumofnumbers(n))

#ques
def power(a,b):
    if b==0:
        return 1
    
    ans = a*power(a,b-1)
    return ans
a = int(input("enter base"))
b = int(input("enter power"))
print(power(a,b))

#ques
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
n = int(input("enter number"))
for i in range(1,n+1):
     print(fibonacci(i))
    




