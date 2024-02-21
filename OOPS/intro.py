#*************basic Class and Object*******************

class Car:
    def __init__(self,user_brand,user_model):
            self.brand=user_brand
            self.model=user_model
    def full_name(self):
          return f"{self.brand} {self.model}"
    
    def fuel_type(self):
          return "Petrol or Diesel"
    
    # *************** Static Method *********

    @staticmethod
    def general_description(): # no need to use self coz self connects class and object and in satatic method we dont need to connect object or instance 
          return "Cars are means of transport"
    

my_car=Car("Toyota","Innova")
# print(my_car.brand)
# print(my_car.full_name())


#*****************Inharitance****************

class ElectricCar(Car):
      def __init__(self, user_brand, user_model,battery_size):
            super().__init__(user_brand, user_model)
            self.battary_size=battery_size
      def fuel_type(self):
          return "battery"


my_tesla=ElectricCar("tesla","Model s","85kWh")

print(my_tesla.battary_size)
print(my_tesla.full_name())


#*************Encapsulation********************* to make variables private



class Mohit:
      def __init__(self,name,brand) :
            self.__name=name #first i made name private to make readonly
            self.__brand=brand 

      def get_brand(self):
            return self.__brand+" !"
      
      @property
      def name(self):
       return self.__name

mohit=Mohit("Mohit","Rajaram")

print(mohit.get_brand())

#*********polymorphism************ Same method gives different output 

print(my_car.fuel_type())
print(my_tesla.fuel_type())


#********use decorator to make something read only**************
print(mohit.name)
 


#************multiple inheritance*********

class Battery:
     def battery_info(self):
          return "This is Battery"

class Engine:
     def engine_info(self):
          return "this is Engine"


class ElectricCarTwo(Battery,Engine):
     pass

my_new_tesla=ElectricCarTwo()

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
     


    
