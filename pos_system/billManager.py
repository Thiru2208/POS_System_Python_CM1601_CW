import json
import os

class BillManager:
    def __init__(self):
        self.billsFile = 'bills.json'

    def loadBills(self):
        """Safely load bills from JSON file."""
        if os.path.exists(self.billsFile):
            with open(self.billsFile, 'r') as file:
                return json.load(file)
        else:
            return {}

    def saveBills(self, billsData):
        """Safely save bills to JSON file."""
        with open(self.billsFile, 'w') as file:
            json.dump(billsData, file, indent=4)

    def finalizeBill(self, basket):
        """Save the basket as a finalize bill."""
        if not basket:
            print("Basket is empty. Cannot finalize bill.\n")
            return

        billsData = self.loadBills()
        billNo = str(len(billsData)+1)

        billsData[billNo] = basket.copy()
        self.saveBills(billsData)
        print(f"Bill No. {billNo} has been saved successfully.\n")
        basket.clear()

    def searchBill(self):
         """Search a bill based on user input Bill Number."""
         billsData = self.loadBills()
         billNo = input("Enter Bill Number to search:")

         if billNo in billsData:
             print(f"\n--- Bill No: {billNo} Details ---")
             for idx, item in enumerate(billsData[billNo], start=1):
                 print(f"{idx}. {item}")
             print()
         else:
             print("No such bill.\n")