class student:
    def __init__(self, name): #class contructor can be used instead of set name and get namwe
        print(name)
        self.name = name

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
student1 = student()
student1.set_name("shehnaaz")
print(student1.get_name())

student2 = student()
student2.set_name("ravi")
print(student2 .get_name())


class rectangle:
    def __init__(self,length, width): #class constructor - we can use it instead of set dimensions 
        print(f"a rectangle of length: {length } amd width: {width} is given")
        self.length = length 
        self.width = width
    
    def set_dimensions(self,length,width):
        self.length = length
        self.width = width 

    def area(self):
       return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
# # recreating class
rectangle1 = rectangle(4,5)
# rectangle2 = rectangle(3,4)
# rectangle3 = rectangle(5,6)
rectangle1.set_dimensions(4,5)
print("The length and width of ractangle is :",rectangle1.length , rectangle1.width)
print("Area of rectangle :", rectangle1.area())
print("Perimeter of rectangle :",rectangle1.perimeter())


    