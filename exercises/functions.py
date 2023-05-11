#arbitrary arguments  - add an * before a parameter in a function to pass more than one argument to the function
def my_function (*kids):
    print ("The youngest child is " + kids[2])

#keyword arguments (kwargs) - sends values with key = value pairs
def my_function1(child1,child2,child3):
    print ("The youngest child is " + child3)
    #Calling  my_function1(child1="grown",child2="healthy",child3="playful")
    #output   The youngest child is playful
   
#Arbitrary keyword arguments ** kwargs
#allows one to add as many keyword arguments in the function using **before the parameter 
def my_function2(**kid):
    print(f"His last name is {kid}")
    
    
    