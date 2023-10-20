#inheritance is one of the basic properties of oops 
#where one class can inheritance the properties of another class

class class1():
    
    def class11(self):
        print("This is class1")

class class2(class1):

    def class22(self):
        print("This is class2")

class class3(class2):

    def class33(self):
        print("This is class3")


c3=class3()
c3.class33()
c3.class11()
c3.class22()