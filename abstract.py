#abstraction is one of the fundatmental properties of OOPs
#where the method are without body and we can modify it 

import abc

class pwp():

    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignment(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass

class myown(pwp):

    def student_details(self):
        print("My own student")

    def student_assignment(self):
        print("My own student assignment")

class other(pwp):

    def student_details(self):
        print("This is other student details")
    
    def student_assignment(self):
        print("This is other student assinment")


own=myown()
own.student_assignment()
own.student_details()