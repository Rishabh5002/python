num = int(input("enter a number"))

# #ques1
if num >= 0:
    print("positive")
else:
    print("negative")

# #ques2
if num%2==0:
    print("number is even")
else:
    print ("number is odd")

# #ques3
cp = int(input("enter cost price"))
sp = int(input("enter selling price"))
profit = sp-cp
loss = cp-sp

if cp<sp:
    print("seller has made profit",profit)
elif cp==sp:
    print("seller has made neither profit nor loss")
else: 
    print("seller has made loss",loss)
   
# #ques4
marks = float(input("enter your percentage"))
#if marks are between 81 to 100
if marks>80:
    print("very good")
 #if marks are between 61 to 80
elif marks>60:
    print("Good")
#if marks are between 41 to 60
elif marks>40:
    print("average")
#if marks are below 40
else:
    print("fail")

# #ques5
eng_marks = int(input("enter marks"))
maths_marks = int(input("enter marks"))

if eng_marks>80 and maths_marks>80:
    print("Grade A")
elif eng_marks>80 or maths_marks>80:
    print("Grade B")
else:
    print("Grade C")

# #ques6
digit = int(input("enter number"))

if digit>=1000 and digit<=9999:
    print("number is of 4 digit")
else:
    print("number is not of 4 digit")

#ques7
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))

if num1>num2 and num1>num3:
    print(num1)
elif num2>num3 and num2>num1:
    print(num2)
else:
    print(num3)

#nested if else
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
elif num2>num3:
    print(num2)
else:
    print(num3)

#ques8
num = int(input("enter number"))
if num%15==0:
    print("number is divisible by 15 also by 3 and 5")
else:
    if num%3==0 or num%5==0:
          print("number is divisble by 3 or 5 but not by 15")
    else:
          print("number is neither divisible by 3 nor 5")
    
#ques9
output = int(input('enter a number'))
print("number is ", "even" if output%2==0 else "odd")

# ques10
weather = input("is it raining?")

if weather== "yes":
    print("take umbrella")
else:
    print("don't take umbrella")

#ques11
#taking input of radius of sphere
radius = float(input("enter radius of sphere"))

#volume of sphere 
volume = 4/3* 3.14156* (radius**3)

print("volume of sphere= ", volume)

#ques12
celcius = float(input("enter temperature"))

fahrenheit = (9/5 * celcius) + 32
print("In fahrenheit temperature is:", fahrenheit) 


 



