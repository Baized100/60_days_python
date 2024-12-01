color=["red","green","black"]
fruit=["mango","jack","jam"]
for x in color:
  for y in fruit:  
    print(x,y) 

name=["naiem","mahamud","shaon","sadek","Baizid"]
village=["amkhola","amtoli", "satla","guronodi","galachipa"]
for x in name:
  for y in village:
    print(x,y)
#Write a qustion words 3 times
serial_number=[1,2,3]
name=["Baizid","shamim","shakwat"]
for i in serial_number:
  print(i)

  for j in name:
    print(j)

rows=4
for x in range(1,rows+1):
  for y in range(1,x+1):
    print("*",end="")
  print("")

list=[["mango","apple","orange"],["Tahsin","mohammad","sara"]]
for i in list:
  print(i)

for i in range(1,5):
  for j in range(i):
      print(i,end="")
  print()