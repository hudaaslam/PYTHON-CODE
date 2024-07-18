
# Rent Calculator

rent = int(input("Enter the Flat Rent: "))
electricity = int(input("Enter the Electricity Bill: "))
food = int(input("Enter the Food Bill: "))
charge = int(input("Enter the Charge per unit: "))
person = int(input("Enter the Person: "))

totalBill = electricity * charge

output = (totalBill + rent + food) // person
print("The Output of the Calculation is " ,output)