userlist=[]
def create():
    print("\nCreate your account ")
    file=open("userdata.txt","r")
    #print(len(file.readline()))
    file.seek(len(file.readline())+1)
    name=input("Enter your username : ")
    for i in file:
        temp=i.split(',')
        userlist.append(temp[0])
    file.close()
    while name in userlist:
        print("Username Already exist try another ")
        name=input("Enter your username : ")
    passw=input("Enter your password : ")
    file=open("userdata.txt", "a")
    file.write(name+","+passw+","+"\n")
    file.close()
    exit()

print("Welcome U all to my food app")
ans=input("Are you new to food app? (y/n): ")
found=1
order=[]
if ans=='y':
    create()
print("\nWelcome back again to our food app ")
   
passw="12345"
while found:
    name=input("Enter your existing user name : ")
    file=open("userdata.txt","r")
    file.seek(len(file.readline())+1) 
    for list in file:
        userlist=list.split(',')
        if(userlist[0]==name):
            print("Name Found ")
            passw=userlist[1]
            found=0
            break
    if found==1:
        print("Name does not exist ")
        ans=int(input("\n1.Create new \n2.Try again"))
        if ans==1:
            create()
    
# while True:
#     for a in file:
#         temp=a.split(',')
#         print(temp[0:])
#         if name in temp:
#             print("Found ur username ")
#             passw=temp[1]
#             ans=1
        
#     else:
#         print("User name does not exists")
#         ans=int(input("Would you like to 1.create a new user or 2.try again"))
#         if ans==1:
#             create()
#         else :
#             continue
#     if(ans==1):
#         break
i=1
while i<=3:
    passe=input("Enter your password : ")
    if passe==passw:
        print("Successfully ")
        break
    else:
        print("Try Again ")
        i=1+1
else :
    print("Failed after trying 3 times ")
while passe==passw:
    print("\nOrder section ")
    ans=input("Would u like to order (y/n) : ")
    c=int(input("Enter how many dishes would u like to order : "))
    if ans=="y":
        for i in range(1,c+1):
            dish=input("Enter the dish {} : ".format(i))
            order.append(dish)
    else:
        print("over")
        break
    


