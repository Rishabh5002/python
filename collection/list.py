fruits = ["apple", "banana", "guava", "cherry"]
print(fruits)

print(type(fruits))
print(len(fruits))
print("banana" in fruits)

# accessing element in list
print(fruits [3])
print(fruits [-2])

print(fruits [1:2])

#add element in list 
fruits.append("papaya")
print(fruits)
fruits.insert(2,"kiwi")
print(fruits)
list2 = [20,30,40,50]
fruits.extend(list2)
print(fruits)

#remove element
fruits.remove("banana")
print(fruits)
fruits.pop(2)
print(fruits)

#changing element
fruits[2] = 'KELA'
print(fruits)

#list comprehension
list1 = [10,30,60,57,47,28,89,23,13,2,18]
list2 = [i for i in list1 if i>25]
print(list2)

list2 = list1.copy()
print(list2)
list3 = list1 + list2
print(list3)
list3.sort(reverse=True)#descending
print(list3)

list3 = [23,65,19,90]
list3[0] = 19
list3[2] = 23
print(list3)

#ques
n = int(input("enter size of list:"))

list = []
for i in range(n):
    num = int(input())
    list.append(num)
    
idx1 = int(input("enter idx1"))
idx2 = int(input("enter idx2"))

#swapping values
temp = list[idx1]
list[idx1]= list[idx2]
list[idx2]= temp
print(list)

