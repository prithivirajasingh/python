#!/usr/bin/env python
import datetime

# Declarations for customization
# Set the applicable year for discount
discountYear = 2022
# Set the applicable week for discount
discountWeek = 11
# Set the applicable discount percentage
discountPercent = 10
# Set this to zero if there are no offers
offersRunning = 1
# Append additional offers if applicable
offerText = "Offer: Buy 2 tins of soup and get one loaf of bread for half price."
offerText += "\nOffer: 10% off on Apples for this week."

# Declarations for code functioning
price = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples': 1.00}
option = -1
qty = 0
halfPricedBread = 0
discountFlag = 0
soupQty = 0
breadQty = 0
milkQty = 0
applesQty = 0
subTotal = 0
total = 0
itemDiscount = 0
totalDiscount = 0
discountText = ""
temp = 0

myDate = datetime.date.today()
year, weekNum, dayOfWeek = myDate.isocalendar()
# print(weekNum)
if year == discountYear and weekNum == discountWeek:
    discountFlag = 1
discountMultiplier = (100 - discountPercent) / 100
# print(discountMultiplier)
if offersRunning == 1:
    introText = ", price and offer"
else:
    introText = " and price"

print("Welcome to our online store!\nPlease find the product ID{0} details below.\n".format(introText))
if offersRunning == 1:
    print(offerText)
print("{:<15} {:<15} {:<10}".format('PRODUCT ID', 'DESCRIPTION', 'PRICE'))
for keys, values in price.items():
    temp += 1
    print("{:<15} {:<15} {:<10}".format(temp, keys, values))
# exit()
while option != 0:
    option = -1
    try:
        option = int(input("\nPlease enter the product ID to add to cart, '0' to checkout: "))
    except:
        pass
    if option == 0:
        pass
    elif option == 1:
        try:
            qty = int(input("You have chosen Soup. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        soupQty += qty
        qty = 0
        # print(soupQty)
    elif option == 2:
        try:
            qty = int(input("You have chosen Bread. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        breadQty += qty
        qty = 0
    elif option == 3:
        try:
            qty = int(input("You have chosen Milk. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        milkQty += qty
        qty = 0
    elif option == 4:
        try:
            qty = int(input("You have chosen Apples. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        applesQty += qty
        qty = 0
    else:
        print("Invalid input. Please try again!")

if soupQty > 0:
    halfPricedBread = soupQty // 2
    subTotal += soupQty * price['Soup']
    total = total + subTotal

if breadQty > 0:
    if breadQty > halfPricedBread:
        subTotal = ((breadQty - halfPricedBread) * price['Bread']) + (halfPricedBread * price['Bread'] / 2)
    else:
        subTotal = breadQty * (price['Bread'] / 2)
    itemDiscount = (breadQty * price['Bread']) - subTotal
    if itemDiscount > 0:
        discountText += "Savings on half price for {} loafs of bread: {:.2f}\n".format(halfPricedBread, itemDiscount)
    totalDiscount += itemDiscount
    total = total + subTotal

if milkQty > 0:
    subTotal = milkQty * price['Milk']
    total = total + subTotal

if applesQty > 0:
    if discountFlag == 1:
        subTotal = (applesQty * price['Apples']) * discountMultiplier
        itemDiscount = (applesQty * price['Apples']) - subTotal
        discountText += "Savings on 10% off for Apples: {:.2f}\n".format(itemDiscount)
        totalDiscount += itemDiscount
    else:
        subTotal = (qty * price['Apples'])
    total = total + subTotal

if discountText == "":
    discountText = "(No offers available)"
print("\nSubtotal: £{:.2f}".format(total + totalDiscount))
print(discountText)
print("Total price: £{:.2f}".format(total))

