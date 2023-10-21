class learn():

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
# Details is class method where first parameter is class 
# and we need to use @classmethod to declare it as classmethod
# the advantage of classmethod is that we can directly access it
# through class.classmethod we dont need to create instance
    @classmethod
    def details(cls,name,age): 
        return cls(name,age)
    
    def display(self):
        print(self.name,self.age)


#accessing the display method with the help of classmethod
learn.details("Pradeep",18).display()


#another way to access the method display is by creating object
learn_object=learn("Chandra",19)
print("Accessing through learn class instance")
learn_object.display()


# How to declare a function outside of a class and 
# declare it as the class method 
# it is simple we need to do 
# classname.name_that_you_want_to_call_the_function=classmethod(function name that you want to add as the class method )


def demo(cls,course_name):
    print("Course name is: ",course_name)

learn.demo=classmethod(demo)
#we make the demo method class method of the class learn
#now we can access it through classname.demo

learn.demo("java")
