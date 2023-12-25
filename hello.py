#print ("hello world!")
 
print ("hello,\n this is rishabh")
print (" nothing to type")

#string
name = "rishabh\n"
print (type (name))

#float
height = 5.6
print (type (height))

#integer
age = '14\n'

#boolian 
is_student = True
percentage = 98.5
print (name,height,age,is_student )

height = 5.9
print (height)
percentage = 97
 
print ("my name is" + name + "my age is" , age)
print (" my height is" , height ,"I am a student is" ,is_student)
print ("my percentaeg has changed to",percentage -1.5 )

# print with separator
print(name, height, age, percentage,is_student, sep="__")

x = 1
y = 2
z = 5
print(x,y,z,sep="   ")

char = "hey there! how beautiful the day is."
char = 'b'
print(len(char))
print(char)
print(ord (char))

ascii = 97
print(chr(ascii))

#input
name = input( "enter your name")
rollno = int(input("enter your id"))

print (name)
print(rollno)

#operator
x = int(input ("enter number 1"))
y = int(input ('enter number 2'))

#arithmatic operator
sum = x+y
sub = x-y
multiply = x*y 
divide = x/y
power = x**y
floor_divide = x//y
print (" sum of these two numbers is", sum)
print(sum, sub, multiply, divide, power,floor_divide)

#comparison operator
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y) 

 #logical operators
exp1 = 2>1
exp2 = 5<3
print("exp1 and exp2", exp1 and exp2)
print("exp1 or exp2", exp1 or exp2)
print("not exp1", not exp1)

#identity operators
x=45
y=56
z=45
print("x and y are same", x is y)
print("x and y are not same", x is not  y)
print("x and z are", x is z)

fruits = ["apple", "banana", "pear", "guava"]
print("cherry is available", "cherry" in fruits)
print("cherry is not available", "cherry" not in fruits)

#bitwise operator
a = 5
b = 7
print("a and b", a&b)
print("a or b", a|b)
print("a xor b", a^b)
print("not a", ~a)
print("right shift of a", a>>1)