#from Operator import Station
#from Operator import Op

class Station:
    def __init__(self,name, heff, power):
        self.name = name
        self.heff = heff
        self.power = power

    def __str__(self):
        return f" Name: {self.name}, Effective: {self.heff}, Power: {self.power}"

class Hatosag:
    def __init__(self,cim):
        self.cim = cim
        self.licences = []
        self.operators = []
        self.threshold = 0

    def add_operator(self,operator):
        van = False
        for item in self.operators:
            if item.__eq__(operator):
                print(f"már van ilyen")
                van= True
              
        if not van:
            self.operators.append(operator)
    
    
    def prod_licence(self,subService, valid,station,operator):
        licence = RadioLicence(subService, valid, station)
        for item in self.operators:
            if item.__eq__(operator):
                break
        else:
            self.operators.append(operator)
        self.licences.append(licence)
        return licence
        
    def generate_invoice(self,filename):
        amount = self.calculate_payment()
        with open(filename, 'w') as file:
            file.write(f"Service: {self.subService}\n")
            file.write(f"Validity: {self.valid}\n")
            file.write(f"Station: {self.station}\n")
            file.write(f"Amount: {amount}\n")
        print("Invoice generated successfully.")


class Op:
    def __init__(self,address,name,):
        self.address = address
        self.name= name
        self.licences = []
        self.stations = []
        
    def request_license(self, subService, valid,station):
        new_license = Hatosag.prod_licence( subService, valid, station,self)
        print(new_license)
        self.licences.append(new_license)
        
        
    def add_station(self, station):
        if station not in self.stations:
            self.stations.append(station)
        else:
            print("már van ilyen") 
        

    def check_operator_licence(self, subservice):
        return subservice in self.licences
    
    def __eq__(self,other):
        return self.address ==  other.address and self.name == other.name
        
        

class RadioLicence:
    def __init__(self,subService,valid,station):
        
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
    budapest = Station("Budapest",10, 20)  
    sopron = Station("Sopron", 100,30)
    hatosag1.add_operator(Op("váliutca", "Béla"))
    operator.request_license("fm", "2024.05.07", sopron)
    license = operator.licences[0] 
    license.generate_invoice("license_invoice.txt")
   


main()
