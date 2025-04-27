from basketManager import BasketManager
from billManager import BillManager
from taxManager import TaxManager
def main():
    basketmanager = BasketManager()
    billmanager = BillManager()
    taxmanager = TaxManager()

    while True:
        print("\n========== Cupcake POS System ==========")
        print("1. Add item to basket")
        print("2. View basket")
        print("3. Remove item from basket")
        print("4. Update item in basket")
        print("5. Finalize bill")
        print("6. Search Bill")
        print("7. View all bills")
        print("8. Generate Tax File")
        print("9. Exit")
        print("=========================================")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.\n")
            continue

        if choice == 1:
            basketmanager.addItem()
        elif choice == 2:
            basketmanager.viewBasket()
        elif choice == 3:
            basketmanager.deleteItem()
        elif choice == 4:
            basketmanager.updateItem()
        elif choice == 5:
            billmanager.finalizeBill(basketmanager.basket)
        elif choice == 6:
            billmanager.searchBill()
        elif choice == 7:
            billmanager.viewAllBills()
        elif choice == 8:
            taxmanager.generateTaxFile()
        elif choice == 9:
            if basketmanager.basket:
                confirm = input("You have items in the basket. Exit without finalizing? (yes/no):").strip().lower()
                if confirm != "yes":
                    continue #return to menu
            print("Exiting POS System. use me again!!\n")
            break
        else:
            print("Invalid choice, please select a number between 1 and 7.\n")

if __name__ == '__main__':
    main() 