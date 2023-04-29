string=str(input("Enter your string"))
output=''
for char in string:
    if char==' ':
        output+="..."
    else:
        output+=char
print(output)