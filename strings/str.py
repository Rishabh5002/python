st = "the unexpected always happen"

# #length of string
print(len(st))

# #find pp in string
print(st.find("pp"))

#print selected index of string
print(st[0:10])

# #replacing word
print(st.replace("always", "never", 1))

# #concatinating strings
st1 = "no matter what "
new_st = st1 + st
print(new_st)

def check_palindrome(str):

    clean_str = (str.replace(" ", "")).lower()
    reverse_str = clean_str[::-1]

    return clean_str==reverse_str

str = input("enter your string")
print(check_palindrome(str))

    


