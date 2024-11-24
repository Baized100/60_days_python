#while loop:is used to excute a block of statements repeatedly until a given a condition is satisfied and when the condition become false the lineimmeditely after the loop in program is excuted
count=0 #inatilazation
while(count<5): #condition
    count=count+1 #increment or decrement
    print("baingladesh",count) #print

for i in range(0,6,1):
    print("boss",i)

i=0
while(i<10):
    i=i+2
    print(i)

data="python of bangladesh"
index=0
while(index<len(data)):
    print(data[index])
    index=index+1

data="baizid i love so much"
data=data.split()
i=0
while(i<len(data)):
    print(data[i])
    i=i+1
s=[1,4,6,8,10,40,50]
total=0
index=0
while(index<len(s)):
    total=total+s[index]
    print(index,total)
    index+=1

#first 10 even number
number=0
while(number<20):
    number=number+2
    print(number)
#first 10 odd number
number=0
while(number<20):
    number=number+3
    print(number)

number=0
while(number<300):
    number=number+10
    print(number,end=",")

number=105
while(number>=7):
    print(number,end=",")
    number=number-7
num=2
sum=0
while(num<20):
    num=num+2
    sum=num+sum
print(sum)


