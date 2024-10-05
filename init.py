class Student:
    def __init__(self,name,hobby):
        self.name=name
        self.hobby=hobby
    def details(self):
        print(f"I am {self.name} and hobby is {self.hobby}.")
        
hemel=Student('Hemel','programming')
rahim=Student('Rahim','traveling')
hemel.details()
rahim.details()