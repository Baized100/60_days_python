x=5
y=10
if x<y:
    print("y greter than x")

else:
    print("good")

#Take values of length and breadth of a rectangle user inpit()and chacks if it is squer or not 
length=int(input("Enter the length value"))
bredth=int(input("Enter the breadth value"))
if length==bredth:
    print("it is square")
else:
    print("it is not suqre")

#take 3 integer valu from user gretest among them
number1=int(input("Enter the number "))
number2=int(input("enter the number"))
number3=int(input("enter the valu"))
if number1>number2 and number1>number3:
    print(" this is gretest number1")
elif number2>number1 and number2>number3:
    print("the gretest number is number2")
else:
    print("the gretest number is number 3")

#3.A student will not be allawed to sit in exam if his /her attendance 

num=int(input("Enter the number"))
if num % 2==0 & num % 5==0:
    print("divitide the number 5 and 2")
else:
    print("number one")

#amount=0
unit=int(input("Enter the current unit"))
if unit<=100:
    amount=0
    print("amount",amount)

elif unit>100 and unit<=200:
    amount=(unit-100)*5
    print("amount",amount)

elif unit>200:
    amount=((unit-100)*10+500)
    print("amount",amount)

else:
    print("!1")