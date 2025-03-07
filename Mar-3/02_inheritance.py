class Cycle:
	def __init__(self):
		self.max_weight = float(input("Enter maximum weight capacity : "))
		self.max_speed = float(input("Enter maximum speed : "))
		self.seat_capacity = int(input("Total number of seat : "))
		
	def output(self):
		print("Maximum Weight Capacity : ",self.max_weight)
		print("Maximum speed : ",self.max_speed)
		print("Seat Capacity : ",self.seat_capacity)
	
class motercycle(Cycle):
	def __init__(self):
		self.brand_name = str(input("Enter Brand name : "))
		self.cylinder = int(input("Enter Cylinder : "))
		self.Power_torque = int(input("Enter Power Torque : "))
		super().__init__()
	def show(self):
		print("Brand Name : ",self.brand_name)
		print("Cylinder : ",self.cylinder)
		print("Power Torque : ",self.Power_torque)
		super().output()
		
	
t1 = motercycle()
t1.show()
	
