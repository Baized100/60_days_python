#foor loop
'''number=[1,2,3,4]
for x in number:
    print(x)

number=range(-100,-9)
for x in number:
    print(x)

number=range(10,1000)
for x in number:
    print(x)

data="bangladesh"
for x in  data:
    print(x)

length=int(input("Enter the length"))
bredth=int(input("Enter the bredth"))
rectangle=(length*bredth)
print(rectangle)

data="bangladesh is good country"
data=data.split()
for x in range(len(data)):
    print(data[x],x)

n=[1,2,3,4,5,6,55,34]
total=0
for i in n:
    total=total+i
    print(total)
#1. Print the first 10 natural numbers using for loop.
for i in range(1,11):
    print(i)

#2.Python program to print all the even numbers within the given range.
n=100
for i in range(0,n,2):
    print(i)
n=100
for i in range(n):
    if i%2==0:
        print(i)

#3.Python program to calculate the sum of all numbers from 1 to a given nu

sum=0
for i in range(1,11):
    sum+=i
print(sum)
#4: Python program to calculate the sum of all the odd numbers within the given range.
n=10
sum=0
for i in range(n):
    if i%2!=0:
        sum+=i
print(sum)

#5: Python program to print a multiplication table of a given number
number=5
for i in range(11):
    print(number,"X",i,"=",5*i)

number=6
for i in range(11):
    print(number,"X",i,"=",6*i)

#6: Python program to display numbers from a list using a for loop.
list=[1,2,3,4,5]
for i in list:
    print(i)