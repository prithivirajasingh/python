#!/usr/bin/env python
import datetime
import pandas as pd
from tabulate import tabulate

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
productsURL = "products.csv"
# productsURL = "https://raw.githubusercontent.com/prithivirajasingh/python/main/shopping_products.csv"
products= pd.read_csv(productsURL)
products.index += 1
products = products.rename_axis('ID')
offerText = "Offer: Buy 2 tins of soup and get one loaf of bread for half price."
offerRefSoup = (products[products.iloc[:, 0]=='Soup'].index.values)[-1] - 1   # This will set the index of Soup
offerRefSoupDivisor = 2   # Buy "2" tins of soup
offerRefBread = (products[products.iloc[:, 0]=='Bread'].index.values)[-1] - 1 # This will set the index of Bread
offerRefBreadMultiplier = 0.5   # get one loaf of bread for "half" price, Eg. 0.2 for 20% discount
offerText += "\nOffer: 10% off on Apples for this week."
offerRefApples = (products[products.iloc[:, 0]=='Apples'].index.values)[-1] - 1  # This will set the index of Apples

# Declarations for code functioning
option = -1
qty = 0
qtyError = 0
discountFlag = 0
subTotal = 0
total = 0
itemDiscount = 0
totalDiscount = 0
discountText = ""
temp = 0

myDate = datetime.date.today()
year, weekNum, dayOfWeek = myDate.isocalendar()
# print(weekNum)
# exit()

if year == discountYear and weekNum == discountWeek:
    discountFlag = 1
discountMultiplier = discountPercent / 100
# print(discountMultiplier)
if offersRunning == 1:
    introText = ", price and offer"
else:
    introText = " and price"

class CartItem:
    def __init__(self, id, qty):
        # CartItem elements contain the below values
        self.id = id
        self.description = products.iat[id, 0]
        self.unitprice = products.iat[id, 1]
        self.quantity = qty
        self.itemprice = self.unitprice * self.quantity
        self.itemdiscount = 0

    def update(self, qty):
        global qtyError
        if self.quantity + qty >= 0:
            self.quantity += qty
            self.itemprice = self.unitprice * self.quantity
        else:
            qtyError = 1

    def __str__(self):
        print("{:<15} {:<15} {:<15} {:.2f}".format(self.description, self.unitprice, self.quantity, self.itemprice))
        return ''

class Cart:
    def __init__(self):
        self.items = {}
        self.subtotal = 0
        self.totaldiscount = 0
        self.total = 0

    def addItems(self, id, qty):
        global qtyError
        # Cart elements are in the format {id: CartItem}
        if not id in self.items and qty > 0:
            self.items[id] = CartItem(id, qty)
        elif id in self.items:
            self.items[id].update(qty)
        else:
            qtyError = 1
        if self.items[id].quantity == 0:
            del self.items[id]

    def evaluate(self):
        global discountText
        if len(self) == 0:
            self.subtotal = 0
            self.totaldiscount = 0
            self.total = 0
            return
        halfPricedBread = 0
        discountText = ""
        if offerRefSoup in self.items:
            halfPricedBread = self.items[offerRefSoup].quantity // offerRefSoupDivisor
        if offerRefBread in self.items:
            if self.items[offerRefBread].quantity > halfPricedBread:
                self.items[offerRefBread].itemdiscount = halfPricedBread * self.items[offerRefBread].unitprice * offerRefBreadMultiplier
            else:
                self.items[offerRefBread].itemdiscount = self.items[offerRefBread].quantity * self.items[offerRefBread].unitprice * offerRefBreadMultiplier
            if self.items[offerRefBread].itemdiscount > 0:
                discountText += "Savings on half price for {} loaf(s) of bread: {:.2f}\n".format(halfPricedBread, self.items[offerRefBread].itemdiscount)
        if offerRefApples in self.items and discountFlag == 1:
            self.items[offerRefApples].itemdiscount = self.items[offerRefApples].quantity * self.items[offerRefApples].unitprice * discountMultiplier
            if self.items[offerRefApples].itemdiscount > 0:
                discountText += "Savings on 10% off for Apples: {:.2f}\n".format(self.items[offerRefApples].itemdiscount)
        self.subtotal = 0
        self.totaldiscount = 0
        for keys in self.items:
            self.subtotal += self.items[keys].itemprice
            self.totaldiscount += self.items[keys].itemdiscount
        if offersRunning == 1:
            self.total = self.subtotal - self.totaldiscount
        else:
            self.total = self.subtotal
        return self.total

    def __len__(self):
        return len(self.items)

    def __str__(self):
        global discountText
        print("\n\nCART DETAILS:")
        print("{:<15} {:<15} {:<15} {:<15}".format('DESCRIPTION', 'UNIT PRICE', 'QUANTITY', 'PRICE'))
        for keys in self.items:
            print(self.items[keys], end='')
        print("\nSubtotal: £{:.2f}".format(self.subtotal))
        if discountText == "" or offersRunning == 0:
            discountText = "(No offers available)"
        print(discountText)
        print("Total price: £{:.2f}".format(self.total))
        return ''

def printToConsole():
    for i in range(1, 50):
        print('\n')
    print("Welcome to our online store!\nPlease find the product ID{} details below.\n".format(introText))
    if offersRunning == 1:
        print(offerText)
    print(tabulate(products, headers='keys', showindex=True, tablefmt='psql', numalign='left', floatfmt=".2f"))
    print(cart)

cart = Cart()
printToConsole()

while option != 0:
    try:
        option = int(input("\nPlease enter the product ID to add to cart, '0' to checkout: "))
    except:
        print("Invalid input. Please try again!")
        continue
    if option == 0:
        pass
    elif option <= products.shape[0]:
        try:
            qty = int(input(f"You have chosen {products.iat[option - 1, 0]}. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        cart.addItems(option - 1, qty)
        cart.evaluate()
        printToConsole()
        if qtyError == 1:
            print("Invalid input. Please try again!")
            qtyError = 0
        qty = 0
    else:
        print("Invalid input. Please try again!")

printToConsole()
exit()
