class mysamplecls:

    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place


    def add_age(self):
        self.age=self.age+1


    def Relocate(self,place):
        self.place=place


    def Display(self):
        print("\nName:- "+self.name)
        print("Age :-"+str(self.age))
        print("Place :-"+self.place)


x=mysamplecls("Arun",26,"EKM")
y=mysamplecls("Akhil",23,"TVM")
x.Display()
y.Display()
x.add_age()
x.Relocate("EKM")
x.Display()

