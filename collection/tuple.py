fruits  = ("apple", "banana", "lichi")
print(type(fruits))
print(fruits)

#transverse tuple
for i in fruits:
    print(i)

#concatenate tuple
more_fruits = ("papaya", "melon", "chikoo", "orange")
print(fruits + more_fruits)

#unpacking a tuple
input_tuple = (1,2,3,4,5,6)
list= []

# #reversing tuple
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)#type casting
print(output_tuple) 



