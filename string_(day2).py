#input funcation
'''data="baizid"
print(type(data))
x=int(input("entr the data" ))
y=int(input("inter the data" ))

print(x+y)
print(type(x+y))

number1=float(input("enter the number"))
number2=float(input("enter number"))
print(number1+number2)'''
#string
data="python bangladesh baizid"
print(type(data))
print(len(data))

string="banglades is good country bangladesh bangladesh"
print(string.count("bangladesh"))

data="bangladesh is good country"
print(data.find("is"))

print(data.index("good"))
print(data.find("no"))
#print(data.index("yes")) no output is index
variable="BAngladesh is"
print(variable.lower())#convart all lowercase
print(variable.upper())#covart all uppercase
print(variable.capitalize())#covart only 1st uppercase
print(variable.swapcase())
print(variable.title())
print(variable.isupper())#every letter is upper
print(variable.islower())#every letter is lower
print(variable.split())#convart the list
print(variable.center(100)) 
print(variable.replace("is","go")) #replace the data

x=20
y=30
z=x+y
print("i have ",z,"taka")
print("i have{}taka".format(z))#format string