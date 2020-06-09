def manager():
    l=input("Login:")
    p=input("Password:")
    if(l!="abc" or p!="124"):
        print("Try again")    
    else:    
        print("Choose\n1.Employee details\n2.Employee salary")
        c=int(input("Enter your choice:"))
        if(c<=0 and c>3):
            print("try again")
        else:
            if(c==1):
                file="employee details1.txt"
                f=open(file,'r+')
                text=f.read()
                print(text)
                f.close()
            elif(c==2):
                file="employee details1.txt"
                f=open(file,'r+')
                text=f.read()
                print(text)
                f.close()
    return()
print("welcome",manager())

print("hello customer")

print("welcome to our restaurant")

dict={'idly':12,'dosa':15,'specialdosa':30,'familydosa':50,'gheedosa':35,'naan':40,'puri':20,'pannerbuttermasala':60,'kulcha':40,'mushroom paratha':25,'paratha':10,'chilliparatha':25,'pongal':20,'noodles':30,'pizza':50,'cheesepizza':60,'chillipizza':50,'burger':45,'sanwich':35,'cutlet':10,'pavbhaji':45,'mushroom':35,'chocobar':20,'vanilla icecream':10,'butterscotch':15}
print(dict)
print('FoodItems\t\t Cost')
for item, cost in dict.items():
    print('{:<20}\t\t {:<20}'.format(item, cost))
cost = 0
choice = 'y'

while(choice == 'y'):

    print("enter the food of our choice:")
    f=str(input())
    print("enter quantity:")
    n=int(input())
    cost += dict[f]*n
    print(dict[f],"*",n,"=",dict[f]*n)
    print(cost)
    print("Do you wish to continue ordering? (y/n):")
    choice=str(input())

    
print("Your total amount is Rs.",cost)
print("thankyou")
