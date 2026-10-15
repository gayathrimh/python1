import random
'''
1 for snake
-1 for water
0 foe gun
'''

computer=random.choice([-1,0,1])
youstr=input("enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"snake",0:"gun",-1:"water "}

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("draw")
else:

    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")