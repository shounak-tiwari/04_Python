import math

class Area:
    def __init__(self, shape):
        self.shape = shape  # Store shape type
        
        match shape:
            case "rectangle":
                self.length = float(input("Enter the length: "))
                self.breadth = float(input("Enter the breadth: "))
            
            case "triangle":
                self.s1 = float(input("Enter side 1: "))
                self.s2 = float(input("Enter side 2: "))
                self.s3 = float(input("Enter side 3: "))
            
            case _:
                print("Invalid shape!")
                self.shape = None


# Create object
a1 = Area("triangle")
