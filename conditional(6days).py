year=int(input("Enter the salary"))
if year>10:
    print("10%")
elif year >= 6 and year <= 10:
    print("8%")
elif year<6:
    print("5%")

#A company decide to give bonus to employee according to following criteria
year=int(input("Enter the exprence"))
if year>10:
    print("10%")
elif year >= 6 and year <= 10:
    print("8%")
elif year<6:
    print("5%")
#Write a program to check Wether an years is leep year or not
year=int(input("Enter the input"))
if year%100==0:
  if year%400==0:
    print("Enter the leep year")
  else:
    print("Enter the not leep year")
else:
    if year%4==0:
        print("Enter the leep year")
    else:
        print("Enter not leep year")
number=int(input("Enter the number"))
if number==1:
    print("sunday")
elif number>1 and number==2:
    print("monday")
elif number>2 and number==3:
    print("Tuiesday")
elif number>3 and number==4:
    print("Wethnasday")
elif number>4 and number==5:
    print("Thasday")
elif number>5 and number==6:
    print("Friday")
elif number>6 and number==7:
    print("satarday")
#Write the logical expression for the followinf a is greter than b and c is greter than d
A=int(input("number"))
B=int(input("number"))
c=int(input("number"))
d=int(input("number"))
if A>B:
    print("A is greter than B")
elif c<d:
    print("C is greter than D")

#Write a program to cheek Whether a person is senior citizen or not
age=int(input("Enter the enput"))
if age>60:
    print("Senior citizen")
else:
    print("not senior citizen")

#largest number
number1=int(input("Enter The number"))
number2=int(input("Enter The number"))
if number1>number2:
    print("The gretest number 1")
elif number1<number2:
    print("The grestest  number 2")