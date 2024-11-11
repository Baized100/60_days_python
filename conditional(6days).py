year=int(input("Enter the salary"))
if year>10:
    print("10%")
elif year >= 6 and year <= 10:
    print("8%")
elif year<6:
    print("5%")