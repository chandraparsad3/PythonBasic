def deco(fun): # A simple decorator function
    def inner_deco(): #fun is the function that you want to decorate
        print("This is Starting")
        fun()
        print("This is End")
    return inner_deco


@deco # you have to call the decortor function above the function that you want to decorate using @decoratorfunctionanme
def test1():
  print(5+6)

test1()


#Second decorator program

import time

def timer(fun):
   def inner_timer():
      start=time.time()
      fun()
      end=time.time()
      print(end-start)
   return inner_timer

@timer
def test2():
   sum=0
   for i in range (0, 10000000):
      sum=i+sum
      sum=sum-i
      sum=sum*i
      sum=sum+0
    
   print(sum)
   
test2()

