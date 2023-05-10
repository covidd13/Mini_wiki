greeting=str(input(">"))
greeting=greeting.strip()

if 'hello' in greeting.casefold():
    print("$0")
elif greeting[0].casefold()=="h":
    print("$20")
else:
    print("$100")

