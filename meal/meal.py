import datetime
b_start=datetime.time(7,0)
b_end=datetime.time(8,0)
l_start=datetime.time(12,0)
l_end=datetime.time(13,0)
d_start=datetime.time(18,0)
d_end=datetime.time(19,0)

user=input("What time is it?")

user_time=datetime.datetime.strptime(user,"%H:%M").time()

if b_start<user_time<b_end:
    print("breakfast time")
elif l_start<user_time<l_end:
    print("lunch time")
elif d_start<user_time<d_end:
    print("dinner time")
else:
    pass

def time_to_float(user_time):
    hours,minutes=map(int,user_time.split(":"))
return hours+'.'+(minutes/5)