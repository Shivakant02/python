#Movie ticket pricing(if age<=18 8$)

age=int(input("Enter the age\n"))
day=str(input("Enter the day\n"))

price=12 if age>=18 else 8


if day=="wednessday" :
        price-=2

print("Ticket price for you is $",price)
