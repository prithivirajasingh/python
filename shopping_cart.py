#!/usr/bin/env python
import datetime

def clearScreen():
    for i in range(1,100):
        print('\n')
    print("Please find the product ID and price below.\n1.Soup:£0.65\t2.Bread:£0.80\t3.Milk:£1.30\t4.Apples:£1.00\n")

price = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples': 1.00}
discountYear = 2022
discountWeek = 11
option = -1
soupQty = 0
breadQty = 0
milkQty = 0
applesQty = 0
halfPricedBread = 0
subTotal = 0
total = 0

myDate = datetime.date.today()
year, weekNum, dayOfWeek = myDate.isocalendar()
#print(weekNum)
print(year)
if year == discountYear and  weekNum == discountWeek:
    discountFlag = 1

print("Welcome to our online store!\nPlease find the product ID and price below.\n1.Soup:£0.65\t2.Bread:£0.80\t3.Milk:£1.30\t4.Apples:£1.00\n")
while option != 0:
    option = int(input("Please enter the product ID. Enter '0' to checkout: "))

    if option == 1:
        qnty = int(input("You have chosen Soup. Please enter the quantity: "))
        halfPricedBread = qnty // 2
        print(halfPricedBread)
        subTotal = qnty * price['Soup']
        clearScreen()
        print("Item subtotal: {:.2f}".format(subTotal))
        total = total + subTotal
        print("Total: {:.2f}".format(total))
    elif option == 2:
        qnty = int(input("You have chosen Bread. Please enter the quantity: "))
        if qnty > halfPricedBread:
            subTotal = ((qnty - halfPricedBread) * price['Bread']) + (halfPricedBread * price['Bread'] / 2)
        else:
            subTotal = qnty * (price['Bread'] / 2)
        clearScreen()
        print("Item subtotal: {:.2f}".format(subTotal))
        total = total + subTotal
        print("Total: {:.2f}".format(total))
    elif option == 3:
        qnty = int(input("You have chosen Milk. Please enter the quantity: "))
        subTotal = qnty * price['Milk']
        clearScreen()
        print("Item subtotal: {:.2f}".format(subTotal))
        total = total + subTotal
        print("Total: {:.2f}".format(total))
    elif option == 4:
        qnty = int(input("You have chosen Apples. Please enter the quantity: "))
        if discountFlag == 1:
            subTotal = (qnty * price['Apples']) * 0.9
        else:
            subTotal = (qnty * price['Apples'])
        clearScreen()
        print("Item subtotal: {:.2f}".format(subTotal))
        total = total + subTotal
        print("Total: {:.2f}".format(total))

print("Your cart total is: {:.2f}".format(total))

