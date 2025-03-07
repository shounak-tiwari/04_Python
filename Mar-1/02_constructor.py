# parameterize constructor 


class Record:
    def __init__(self,Name,Contact):
        self.Name = Name
        self.Contact = Contact
    def display(self):
        print("Name : ",self.Name)
        print("Contact  : ",self.Contact)
    

p = Record("Ashwin",8718828288)

p.display()