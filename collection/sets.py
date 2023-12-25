names = {"ria", "mia", "kia", "sia", "Tia"}
names.add("jiya")
print(names)

#add another sequence
name_list = ("Mike", "casie", "tony")
names.update(name_list)
print(names)

#remove element
names.discard("ria")
print(names)

#union intersection and symmetric difference
l1= [1,5,10,20,40,80]
l2 = [6,7,20,80,100]

s1 = set(l1)
s2 = set(l2)
s1= s2.union(s1)
print(s1)

#ques
n = int(input("enter size of list1:"))

list1 = []
for i in range(n):
    num = int(input())
    list1.append(num)
    
m = int(input("enter size of list2:"))
list2 = []

for j in range(m):
   num2 = int(input())
   list2.append(num2)

s1 = set(list1)
s2 = set(list2)

s1.intersection_update(s2)
print(s1)
print(list1)
print(list2)

#creating a dictionary
phone ={
"joy": 8876789,
"jane":8779127,
"mike":7832982,
"cassey" :7898903,
"rody": 9878454
}

print(phone)
print(type(phone))

# add dictionary values
num = {
"a": 30,
"b": 20,
"c": 25,
"d": 45,
}
print(sum(num.values()))

#ques
text = input("enter your text:")
n = int(input("enter digit:"))

 #creating dictionary 
l1 = "abcdefghijklmnopqrstuvwxyz"
l2 = 'zyxwvutsrqponmlkjihgfedcba'
dict1 = dict(zip(l1,l2))

 #finding part of dictionary we need to do mirror 
prefix = text[0:n-1]
suffix = text[n-1:]

 #finding mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

res = prefix + mirror
print("the result is", res)
    