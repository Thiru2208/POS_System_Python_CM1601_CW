from operator import index


class BasketManager:
    def __init__(self):
        self.basket = []

    def addItem(self):
        print("\n--Add New Item--")
        item = {}

        #Item code
        itemCode = input("Enter Item Code: ").strip()
        if not itemCode:
            print("Item Code cannot be empty.\n")
            return
        item['itemCode'] = itemCode

        #Item Name
        itemName = input("Enter Item Name: ").strip()
        if not itemName:
            print("Item Name cannot be empty.\n")
            return
        item['itemName'] = itemName

        #Sale Price
        while True:
            try:
                salePrice = float(input("Enter Sale Price: "))
                if salePrice <= 0:
                    print("Sale Price must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid input! Sale Price must be a number.")
        item['salePrice'] = salePrice

        #Discount
        while True:
            try:
                discount = float(input("Enter Discount: "))
                if discount < 0:
                    print("Discount cannot be negative.\n")
                else:
                    break
            except ValueError:
                print("Invalid input! Discount must be a number.\n")
        item['discount'] = discount

        #Quantity
        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.\n")
                else:
                    break
            except ValueError:
                print("Invalid input! Quantity must be an integer.\n")
        item['quantity'] = quantity

        #Line total calculation
        item['lineTotal'] = item['salePrice'] * item['quantity']

        self.basket.append(item)
        print("Item added successfully!\n")

    def viewBasket(self):
        if not self.basket:
            print("Basket is empty!\n")
            return
        print("\n---Current Basket Items---")
        for idx, item in enumerate(self.basket, start=1):
            print(f"{idx}.Item Code: {item['itemCode']}, Name: {item['itemName']}, "
              f"Sale Price: Rs.{item['salePrice']}, Discount: {item['discount']}%, "
              f"Quantity: {item['quantity']}, Line Total: Rs.{item['lineTotal']}")
        print()

    def deleteItem(self):
        self.viewBasket()
        if not self.basket:
            return
        try:
            index = int(input("Enter Item Index: ")) -1
            if 0 <= index < len(self.basket):
                removeItem = self.basket.pop(index)
                print(f"{removeItem['itemName']} removed successfully!\n")
            else:
                print("Invalid Item Index! Please try again.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number. \n")

    def updateItem(self):
        self.viewBasket()
        if not self.basket:
            return
        try:
            index = int(input("Enter Item Index: ")) -1
            if 0 <= index < len(self.basket):
                item = self.basket[index]
                print(f"Updating Item {item['itemName']}")
                try:
                    sale_price = float(input("Enter New Sale Price: "))
                    if sale_price <= 0:
                        print("Sale Price must be greater than 0.\n")
                        return
                except ValueError:
                    print("Invalid input! Sale Price must be a number.\n")
                    return
                item['salePrice'] = sale_price

                # Validate new discount
                try:
                    discount = float(input("Enter New Discount: "))
                    if discount < 0:
                        print("Discount cannot be negative.\n")
                        return
                except ValueError:
                    print("Invalid input! Discount must be a number.\n")
                    return
                item['discount'] = discount

                # Validate new quantity
                try:
                    quantity = int(input("Enter New Quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0.\n")
                        return
                except ValueError:
                    print("Invalid input! Quantity must be an integer.\n")
                    return
                item['quantity'] = quantity

                item['lineTotal'] = item['salePrice'] * item['quantity']
                print(f"{item['itemName']} updated successfully!\n")
            else:
                print("Invalid Item Index! Please try again.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number. \n")


