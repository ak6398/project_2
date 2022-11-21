import random
Cnumber=random.randrange(1,101)
userinput=int(input("enter your number"))
if(userinput>Cnumber):
    print("computer number",Cnumber)
    print("your guess no is high")
    print("you win")
elif(userinput<Cnumber):
    print("computer number",Cnumber)
    print("your number is low")
    print("computer win")
else:
    print("computer number",Cnumber)
    print("your number is equal to ",Cnumber)