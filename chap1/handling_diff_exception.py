#there many types of error
#like zero div error,  types error,  value error

try:
    a=int(input("enter a number"))
    c=1/a
except ValueError as e:
    print("Please Enter a Valid Value") 
    print(e)
except ZeroDivisionError as e :
    print("Make Sure You are not Dividing with 0") 
    print(e)      
print("thank for running a code")      