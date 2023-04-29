string=str(input("Enter your string with emoticon"))
for char in string:
    if char=ord(":") and ord(")"):
        string+="😂"
    elif char=="):":
        string+="😢"
    else:
        string+=char
print(string)
