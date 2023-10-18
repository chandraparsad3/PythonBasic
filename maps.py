# <!-- In Python, the map function is a tool that takes a function
# and a list as input. It applies that function to every item 
# in the list and returns an iterator. You can convert this
# iterator into a list, and it will contain the results of 
# applying the function to each item. It's a way to process 
# data in a list more efficiently without writing explicit loops. -->
#map(function_name, input1, input2)
from functools import reduce
l=[1,2,3,4,5]
l2=[5,6,7,8,9]
print(list(map(lambda x,y: x+y ,l,l2)))

def add(x,y):
    return x+y
print(list(map(add,l,l2)))

def multi(x,y):
    return x*y
print(list(map(multi,l,l2)))

print("Reduce: ", reduce(add,l))
print("Multiply: ",reduce(multi,l2))
print("Maximum: ", reduce(lambda x,y: x if x> y else y, l2))

print("Even: ", list(filter(lambda x: x%2==0 ,l)))

l3=["Pradeep","Bhandari","Chandra","Parsad"]
print("Length: ", list(filter(lambda x: len(x)<10, l3)))
