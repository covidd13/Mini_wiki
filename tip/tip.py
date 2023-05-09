def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    string1,string2 = d.split(".")
    return (string1[1:]+'.'+string2[0])


def percent_to_float(p):
    digit1,digit2 = p.split("%")
    digit1=int(digit1)
    return digit1/100



main()
