#ques1
n = int(input("enter n:"))

for _ in range(n):
    print( "*****")

#ques2
n = int(input("enter n:"))

for _ in range(n):
    for i in range(1,n+1):
        print(i, end="")
    print()

#ques3
n = int(input("enter n:"))

for i in range(1, n+1):#for rows
    for j in range(1,i+1): #for columns
     print(j, end="")
    print()


#ques4 
n = int(input("enter n:"))

for i in range(1,n+1):#for row
    #for spaces
    print(" " * (n-i), end="")

    #for printing digit 
    for j in range(1,2*i):
       print(j, end="") 
    print()


