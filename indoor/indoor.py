var1=str(input("Please Enter the string you want to convert"))
var2=''
for char in var1:
    if ord(char)>=65 and ord(char)<=90:
        ord(char)=ord(char)+32
    else:
        pass
    var3=char
    var2+=var3
print(var2)




