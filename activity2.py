units = int(input("Please enter the number of units you consumed: "))
if units < 50:
    amount = units * 2.60
    sub_charge = 25
elif units <= 100:
    amount = 130 + ((units - 50)* 3.25)
    sub_charge = 35
elif units <= 200:
    amount = 130 + 162.50 + ((units - 100)* 5.26)
    sub_charge = 45
else:
    amount = 130 + 162.50 + 226 + ((units - 200)*8.45)
    sub_charge = 75
total = amount + sub_charge
print("\n electricity bill = %.2f" %total)
