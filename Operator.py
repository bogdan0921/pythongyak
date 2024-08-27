class Station:
    def __init__(self, name, heff, power):
        self.name = name
        self.heff = heff
        self.power = power

    def __str__(self):
        return f" Name: {self.name}, Effective: {self.heff}, Power: {self.power}"

class Hatosag:
    def __init__(self, cim):
        self.cim = cim
        self.licences = []
        self.operators = []
        self.threshold = 0

    def add_operator(self, operator):
        van = False
        for item in self.operators:
            if item == operator:
                print(f"már van ilyen")
                van = True
              
        if not van:
            self.operators.append(operator)
    
    def prod_licence(self, subService, valid, station, operator):
        licence = RadioLicence(subService, valid, station)
        for item in self.operators:
            if item == operator:
                break
        else:
            self.operators.append(operator)
        self.licences.append(licence)
        return licence
        
    def generate_invoice(self, licence, filename):
        amount = licence.calculate_payment()
        with open(filename, 'w') as file:
            file.write(f"Service: {licence.subService}\n")
            file.write(f"Validity: {licence.valid}\n")
            file.write(f"Station: {licence.station}\n")
            file.write(f"Amount: {amount}\n")
        print("Invoice generated successfully.")

class Op:
    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.licences = []
        self.stations = []
        
    def request_license(self, hatosag, subService, valid, station):
        new_license = hatosag.prod_licence(subService, valid, station, self)
        self.licences.append(new_license)
        
    def add_station(self, station):
        if station not in self.stations:
            self.stations.append(station)
        else:
            print("már van ilyen") 
        

    def check_operator_licence(self, subservice):
        return any(licence.subService == subservice for licence in self.licences)
    
    def __eq__(self, other):
        return self.address == other.address and self.name == other.name

class RadioLicence:
    def __init__(self, subService, valid, station):
        self.subService = subService
        self.valid = valid
        self.station = station
        
    def calculate_payment(self):
        amount = self.station.heff * self.station.power
        return amount
    
    def __str__(self):
        return f"{self.subService} {self.valid} {self.station}"

def main():
    operator = Op("krisztina korut 39.", "AH")
    hatosag1 = Hatosag("nmhh")
    budapest = Station("Budapest", 10, 20)
    sopron = Station("Sopron", 100, 30)
    hatosag1.add_operator(Op("váliutca", "Béla"))
    operator.request_license(hatosag1, "fm", "2024.05.07", sopron)
    license = operator.licences[0]
    hatosag1.generate_invoice(license, "license_invoice.txt")

main()
