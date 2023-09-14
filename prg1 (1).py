mark1=int(input("enter the tamil mark:"))
mark2=int(input("enter the english mark:"))
mark3=int(input("enter the maths mark:"))
mark4=int(input("enter the science mark:"))
mark5=int(input("enter the cs mark:"))
print(mark1)
print(mark2)
print(mark3)
print(mark4)
print(mark5)
if(mark1>mark2 and mark1>mark3 and  mark1>mark4 and  mark1>mark5):
 print("maximun mark=",mark1)
elif(mark2>mark3 and mark2>mark4 and  mark2>mark5 ):
 print("maximun mark=",mark2)
elif(mark3>mark4  and  mark3>mark5):
 print("maximun mark=",mark3)
elif(mark4>mark5):
 print("maximun mark=",mark4)
else:
 print("maximum mark=",mark5)

if(mark1<mark2 and mark1<mark3 and  mark1<mark4 and  mark1<mark5):
 print("minimun mark=",mark1)
elif(mark2<mark3 and mark2<mark4 and  mark2<mark5 ):
 print("minimun mark=",mark2)
elif(mark3<mark4  and  mark3<mark5):
 print("minimun mark=",mark3)
elif(mark4<mark5):
 print("minimun mark=",mark4)
else:
 print("minimum mark=",mark5)



