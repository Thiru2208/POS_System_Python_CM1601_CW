import json
import os

class TaxManager:
    def __init__(self):
        self.billsFile = 'bills.json'
        self.taxesFile = 'taxes.json'

    def loadBills(self):
        """Load bills from JSON file"""
        if os.path.exists(self.billsFile):
            with open(self.billsFile, 'r') as file:
                return json.load(file)
        else:
            return {}

    def generateChecksum(self, text):
        """Generate a checksum based on character counts."""
        capital = sum(1 for c in text if c.isupper())
        small = sum(1 for c in text if c.islower())
        digits = sum(1 for c in text if c.isdigit() or c == '.')
        return capital + small + digits

    def generateTaxFile(self):
        """Create tax transaction file with checksum."""
        billData = self.loadBills()
        taxRecords = []

        for billNo, items in billData.items():
            for item in items:
                record = item.copy()
                record['billNo'] = billNo

                # Ensure internalPrice is included
                if 'internalPrice' not in record:
                    record['internalPrice'] = 0.0

                # Checksum generation
                recordStr = json.dumps(record)
                record['checksum'] = self.generateChecksum(recordStr)

                taxRecords.append(record)

        with open(self.taxesFile, 'w') as file:
            json.dump(taxRecords, file, indent=4)

        print(f"Tax Transaction File: {self.taxesFile} generated successfully!\n")
