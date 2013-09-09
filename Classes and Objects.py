#define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00 
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
#your code goes here
MyCar1 = Vehicle()
MyCar1.color = "red"
MyCar1.name = "Fer"
MyCar1.value = 60000.0
MyCar1.kind = "convertible"

MyCar2 = Vehicle()
MyCar2.color = "blue"
MyCar2.name = "Jump"
MyCar2.value = 10000.0
MyCar2.kind = "van"

#checking code
print MyCar1.description()
print MyCar2.description()