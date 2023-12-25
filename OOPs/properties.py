#inheritance
class parent:
    def __init__(self):
        self.super_attruibute = True
        print("this is parent class")

class child(parent):
        def __init__(self):
             super().__init__()
             print("this is child class")
             print(self.super_attruibute)

child1 = child()

#ques
class vehicle:
    def __init__(self,capacity):
        self.capacity = capacity

    def fare(self):
        return (self.capacity*100)
    
class bus (vehicle):
    def __init__(self,capacity):
          super().__init__(capacity)
        
    def fare(self):
        vehicle_fare = super().fare()
        maintainance_fare = 0.1* vehicle_fare
        total_fare = vehicle_fare + maintainance_fare
        return total_fare
    
vehicle1 = vehicle(50)
print("total fare of vehicle is:", vehicle1.fare())

bus1 = bus(50)
print("bus fare is:",bus1.fare())

#polymorphism
class animal:
    def speak():
        pass
class dog(animal):
    def speak(self):
        print("barks")

class cat(animal):
    def speak(self):
        print("meow")

class cow(animal):
    def speak(self):
        print("moo")

Dog = dog()
Cat = cat()
Cow = cow()                                              

Dog.speak()
Cat.speak()
Cow.speak()

#compile time polymorphism
#method overloading
class add:
    def sum(self,a,b):
        print(a+b)

    def sum(self,a,b,c):
        print(a+b+c)

#operator overloading
class comple_number:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return comple_number(self.real+other.real, self.img +other.img)
    
c1 = comple_number(1,2)
c2 = comple_number(3,4)
c3= c1 + c2
print(c3.real,"+ i", c3.img)



    



