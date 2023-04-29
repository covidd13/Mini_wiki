var1=str(input("Please Enter the string you want to convert"))
var2=''
for char in var1:
    if ord(char)>=65 and ord(char)<=90:
        cr=ord(char)+32
        var3=chr(cr)
    else:
        var2+=char

    var2+=var3
print(var2)




