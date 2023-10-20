#Encapsulation is basic properties of OOPS
#Encapsulation can be used so that the variable cannot
#be direclty accessed and modified

class car():
    def __init__(self,year,month,speed):
        self.__year=year
        self.__month=month 
        self.__speed=speed

    def setspeed(self,speed):
        self.__speed=speed
    
    def getspeed(self):
        print (self.__speed)
    

c=car(2022,2,235) # car object
c.setspeed(18) #setting the speed through method
c.getspeed()#calling the speed

# print(c.__year) this will throw you error
#you have to access the value in below way
# print(c._car__year)


#---------------------------------------------------------------------------------

class Bank():
    def __init__(self,balance):
        self.__balance=balance #the user cannot direclty access this

    def deposit(self,amount):
        self.__balance+=amount
        print("Your balance is: ", self.__balance)
    
    def withdraw(self,amount):
        self.__balance-=amount
        print("Your remaining amount is: ",self.__balance)

    def getamount(self):
        print("Your balance is: ",self.__balance)


ban=Bank(5000)

ban.deposit(500)
ban.getamount()
ban.withdraw(500)

#This is the perfect example of encapsulation


