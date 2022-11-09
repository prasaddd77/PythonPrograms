# Create class Vehicle with instance variables milage and max_speedand name. Create inner
# class with instance variables‘seating capacity’ and method ‘fare’.Fare for vehicle is 20 times the
# seating capacity. Additional 10% maintenance charges are added to it. Vehicle_info method
# displays milage, max_speed, seating capacity and fare of vehicle.Create two objects bus and
# carofVehicle class.Set the appropriate values for these objects using constructors of enclosing
# class and inner class. Display the information of each object using Vehicle_info method

# class Vehicle():
#     def __init__(self,mileage,max_speed,n,sc) :
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.name = n 
#         self.v1 = self.innerclass(sc)
#     class innerclass:
#         def __init__(self,sc):
#             self.seating_capacity = sc
#             self.fare 
#         def fare(self):
#             f1 = 20*self.seating_capacity
#             fare = f1 + (10/100*f1)
#             return fare
#     def vehicle_Info(self):
#         print("The mileage of the", self.name,"=", self.mileage)
#         print("The max speed of ", self.name,"=",self.max_speed)
#         print("The seating capacity of ", self.name,"=",self.v1.seating_capacity)
#         print("The fare of ", self.name,"=", self.v1.fare())
# bus = Vehicle(45,70,"Tata Punch",30)
# bus.vehicle_Info()

# Create class Vehicle with instance variables milage and max_speedand name.Create two
# child classes bus and car from it.Child classes override the ‘seating_capacity’and ‘fare’method
# from base class vehicle.Default seating capacity of bus is 40 and that of car is 3. Fare for vehicle
# is 20 times the seating capacity. Additional 10% maintenance charges are added to it.
# Vehicle_info method displays milage, max_speed, seating capacity and fare of vehicle.

class Vehicle():
    seating_capacity = 2
    def __init__(self,mileage,max_speed,name) :
        self.mileage = mileage
        self.max_speed = max_speed
        self.name = name
    def fare(self,fare):
        return fare
    def vehicle_Info(self):
        print("The mileage of the", self.name,"=", self.mileage)
        print("The max speed of ", self.name,"=",self.max_speed)
        print("The seating capacity of ", self.name,"=",Vehicle.seating_capacity)
        print("The fare of ", self.name,"=", self.fare())
    
class Car(Vehicle):
    def __init__(self,mileage,max_speed,name) :
        super().__init__(mileage,max_speed,name)
        Vehicle.seting_capacity = 3 
    def fare(self):
        f1 = 20*self.seting_capacity
        fare=f1+(10/100*f1)
        return fare
class Bus(Vehicle):
    def __init__(self,mileage,max_speed,name) :
        super().__init__(mileage,max_speed,name)
        Vehicle.seting_capacity = 20 
    def fare(self):
        f1 = 20*self.seting_capacity
        fare=f1+(10/100*f1)
        return fare

b=Bus(45,70,"Tata")
b.vehicle_Info()

c=Car(50,110,'swift')
c.vehicle_Info()


            

            
                                    