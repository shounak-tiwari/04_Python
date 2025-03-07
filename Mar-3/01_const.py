class Record:
	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance
	
	def __init__(self):
		print("hellow")
		self.name = input("Enter the name of user : ")
		
	def show(self):
		print("The name of student : ",self.name)
		
	
S1 = Record()
S2 = Record()

S1.show()
S2.show()

