def passw():
    print("\nCreate your account ")
    name=input("Enter your username : ")
    passw=input("Enter your password : ")
    return passw

print("Welcome U all to my food app")
ans=input("Are you new to food app? (y/n): ")
i=1
passw='12345'
order=[]
if ans=='y':
    passw=passw()
print("\nWelcome back again to our food app ")
name=input("Enter your existing user name : ")
while i<=3:
    passe=input("Enter your password : ")
    if passe==passw:
        print("Successfully ")
        break
    else:
        print("Try Again ")
else :
    print("Failed after trying 3 times ")
while passe==passw:
    print("\nOrder section ")
    c=int(input("Enter how many dishes would u like to order : "))
    while c!=0:
        for i in range(1,c+1):
            dish=input("Enter the dish {} : ".format(i))
            order.append(dish)
        else:
            break
    print("over")
    break


