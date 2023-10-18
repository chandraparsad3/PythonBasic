class pwpskills: #class pwpskills which contains welcome message functions
    def welcome_msg(self):
        print("Welcome to pwpskills")

rohan=pwpskills() #an object for pwpskills was created
rohan.welcome_msg() #welcome_msg was print


class pwskills1:
    def __init__(self,phoneno,emial,studentid):
        self.phoneno=phoneno
        self.email=emial
        self.studentid=studentid
    def return_student(self):
        return self.studentid,self.email,self.phoneno
    
rohan=pwskills1(12333333,'rohan@gmail.com',233)

print(rohan.return_student())


#self is not a reversed you can used any name. self is just a pointer.