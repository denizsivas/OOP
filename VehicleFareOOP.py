class Vehicle:
    def __init__(self, name, mileage, capacity) :
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 10
    
class Taxi(Vehicle):
        def fare(self):
             amount = super().fare()
             amount += amount * 10 / 100
             return amount
        
Taxi_car = Taxi("BMW", 12, 50)
print("Total fare is:", Taxi_car.fare())