#numeric Data type

'''x=103 #int
y=12.6 #float
z=10+4j #coplex
print(type(x))
print(type(y))
print(type(z))
#int to float
n=float(x)
print(n)

c=int(n)
print(c)
#int to complex
d=complex(c) #complex theke int ba float hbe nah
print(d)

n=complex(input("number"))

#bollien(true,flase)

#sequence data(list,tuple,range)
#list
li=[1,2,3,4,True,(9,8,7)]
print(li[0])
print(li[-1][-3])
print(type(li))

#tuple
tu=(1,2,3,4,5)
print(tu[0:5])
#range
x=range(10) #1st case
print(x)
for i in x:
    print(i)

x=range(5,20) #2nd case
for i in x:
    print(i)

x=range(1,30,3) #3rd case
for i in x:
    print(i)'''

x=range(5,20,-3)
for i in x:
    print(i)

#set
s={1,2,3,4,"baizid"}
print(s)
#dicatnary
dic={
    "unversity":"barishal information techonology",
    "deparment":"Cse"

}
print(dic)

print(type(dic))

print(dic.values())