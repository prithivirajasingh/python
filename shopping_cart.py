#!/usr/bin/env python
import datetime

# Declarations for customization
# Append as many products as needed w
products = {1: ['Soup', 0.65], 2: ['Bread', 0.80], 3: ['Milk', 1.30], 4: ['Apples', 1.00]}
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
offerRef1 = 1  # 1 is product id of Soup
offerRef2 = 2  # 1 is product id of Bread
offerText += "\nOffer: 10% off on Apples for this week."
offerRef4 = 4  # 4 is product id of Apples

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
        self.description = products[id][0]
        self.unitprice = products[id][1]
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

    def evaluate(self):
        global discountText
        if not len(self) > 0:
            return
        halfPricedBread = 0
        discountText = ""
        for keys in self.items:
            if self.items[keys].quantity == 0:
                del self.items[keys]
                break
        if offerRef1 in self.items:
            halfPricedBread = self.items[offerRef1].quantity // 2
        if offerRef2 in self.items:
            if self.items[offerRef2].quantity > halfPricedBread:
                self.items[offerRef2].itemdiscount = halfPricedBread * self.items[offerRef2].unitprice / 2
            else:
                self.items[offerRef2].itemdiscount = self.items[offerRef2].quantity * self.items[offerRef2].unitprice / 2
            if self.items[offerRef2].itemdiscount > 0:
                discountText += "Savings on half price for {} loaf(s) of bread: {:.2f}\n".format(halfPricedBread, self.items[offerRef2].itemdiscount)
        if offerRef4 in self.items and discountFlag == 1:
            self.items[offerRef4].itemdiscount = self.items[offerRef4].quantity * self.items[offerRef4].unitprice * discountMultiplier
            if self.items[offerRef4].itemdiscount > 0:
                discountText += "Savings on 10% off for Apples: {:.2f}\n".format(self.items[offerRef4].itemdiscount)
        self.subtotal = 0
        self.totaldiscount = 0
        for keys in self.items:
            self.subtotal += self.items[keys].itemprice
            self.totaldiscount += self.items[keys].itemdiscount
        if offersRunning == 1:
            self.total = self.subtotal - self.totaldiscount
        else:
            self.total = self.subtotal

    def __len__(self):
        return len(self.items)

    def __str__(self):
        global discountText
        if len(self) > 0:
            print("\nCART DETAILS:")
            print("{:<15} {:<15} {:<15} {:<15}".format('DESCRIPTION', 'UNIT PRICE', 'QUANTITY', 'PRICE'))
            for keys in self.items:
                print(self.items[keys], end='')
            print("\nSubtotal: £{:.2f}".format(self.subtotal))
            if discountText == "" or offersRunning == 0:
                discountText = "(No offers available)"
            print(discountText)
            print("Total price: £{:.2f}".format(self.total))
            return ''
        else:
            return ''

def printToConsole():
    for i in range(1, 100):
        print('\n')
    print("Welcome to our online store!\nPlease find the product ID{0} details below.\n".format(introText))
    if offersRunning == 1:
        print(offerText)
    print("{:<15} {:<15} {:<10}".format('PRODUCT ID', 'DESCRIPTION', 'PRICE'))
    for keys, values in products.items():
        print("{:<15} {:<15} {:<10}".format(keys, values[0], values[1]))
    print(cart)

cart = Cart()
printToConsole()
while option != 0:
    option = -1
    try:
        option = int(input("\nPlease enter the product ID to add to cart, '0' to checkout: "))
    except:
        pass
    if option == 0:
        pass
    elif option in products:
        try:
            qty = int(input(f"You have chosen {products[option][0]}. Please enter the quantity: "))
        except:
            print("Invalid input. Please try again!")
        cart.addItems(option, qty)
        cart.evaluate()
        printToConsole()
        if qtyError == 1:
            print("Invalid input. Please try again!")
            qtyError = 0
        qty = 0
    else:
        print("Invalid input. Please try again!")

cart.evaluate()
printToConsole()
exit()
