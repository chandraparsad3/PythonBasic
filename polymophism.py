#polymophism is one of the properties of OOPS
#Polymophism means multiple forms 
#Polymorphism refers to the ability of a variable, function, or object to take on multiple forms.

def add(a,b):
    print(a+b)

add(1,2)
add("Pradeep ","Bhandari")
#Here calling the same functions but the function is acting differently based on the user input

class web_dev():
    def syllabus(self):#syllabus functions for web_dev class
        print("This is web development course")

class data_science():
    def syllabus(self):#syllabus functions for data_science class
        print("This is web development course")


def display(class_object): #This is the display functions which will display the syllabus functions of which the loop fetch
    for i in class_object:
        i.syllabus()

class_object=(web_dev(),data_science())

display(class_object)


