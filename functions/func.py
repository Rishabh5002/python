def printehello():
    print("hello world")

printehello()

#example
def sumOnetoN(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i 
    return sum

n = int(input("emter n:"))
#call function
output = sumOnetoN(n)
print("the sum of numbers till n is:", output)
n1 = int(input("emter n1:"))
output1 = sumOnetoN(n1)
print("the sum of numbers till n is:", output1)


def add(n1,n2 = 0):
    sum = n1 + n2
    return sum

x = 2 
y = 3
print("the sum is ", add (2,3))#positional arguments

#keyword argument 
print("the sum is", add (n1 = 2, n2 = 3))

#default argumemt
print("the sum is", add (3))

  
def addAllnumbes(*args):
    sum = 0 
    for i in args:
        sum+= i
    return sum
output = addAllnumbes(1,2,3,4,5)
print("the sum is ", output)


def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is" ,y)

studentinfo(name = "rishabh", age = 18, city = "delhi")
studentinfo(name = "niyati", age = 18, city = "himachal")
