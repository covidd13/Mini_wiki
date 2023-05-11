expression=input("Please enter your expression(x,y,z)")
x,y,z=expression.split()
result=eval(x+y+z)
print({":.1f".format(result)})