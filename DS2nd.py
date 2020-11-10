# print("Question number Firest...")

# empty_list=[]
# for x in range(2):
    
#     entry=int(input("enter your number:"))
#     if (entry % 2==0):
#         empty_list.append(entry)

# print("after getting 10 number from user:",empty_list)
# print("there are:",len(empty_list),"even number present in the list")

# print()
# print("Question number 2nd list comprehension...")
# myname=[char  for char in "Vivek"]
# print(myname)



# print()
# print("quetion third  dictnory")
# mydict={}



# n=int(input("entery:"))
# squares={x:x*x for x in range(1,n+1)}
# print(squares) 


# print("using for loop")
# # mydict={}
# for k in range(4):
#     v=k*k
#     mydict[k]=v
# print(mydict)    

# print("")
# print("question no 4... ")
# print("robot")




# # def walking():
# #     iniit=0 
# #     up=5 #5
# #     down=3 #3
# #     left=3 #3
# #     right=2 #2
# #     direction=input("enter direction U D L R:")
# #     dist=int(input("steps uou wanted to go:"))
# #     if direction=="u" or"U" and dist==5:
# #         up=5
# #         iniit+=up
# #     elif direction=="d" or"D" and dist==3:
# #         down=3
# #         iniit-=down
# #     elif direction=="L" or"l" and dist==3:
# #         left=3
# #         iniit-=3
# #     elif direction=="r" or"R" and dist==2:
# #         right=2
# #         iniit+=2
# #     print(iniit)
# # walking()        

# iniit=0  
# up=0 
# down=0 
# left=0 
# right=0 
# for i in range(4):
#     dir=input("enter direction")
#     for  j in range(4):
#         dist=int(input("distance:"))
#     print(dir,dist)    



import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)