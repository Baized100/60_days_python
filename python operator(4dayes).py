#arithmatic operator
num1=122
num2=num1
print(num2)
x=15
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**x)
print(x//y)

#python identy operator
x=10
y=10
z=x is y
print(z)

x=1011
y=x
z=1011
z=x is y
print(z)#identy mulutoh adress neye kaj kore valu neye nai tai true ba false ase
v=x is z
print(v)
v=x is not z
print(v)

#membership operator
list=[1,2,3,4,54]
x=54 in list
print(x)
y=10 in list
print(y)

string="baizid shake is good boy"
z="boy" in string
print(z)

#bitwise operator
x=10
y=5
b=x|y
print(b)

#coparison operator
x=10
y=15
x==y
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

#logical operator(and,or,not)
x=5
y=7
print(x<y and x>y)
print(x<y or x>y)

#assignment operator
x=10
x+=4
print(x)
x-=5
print(x)