'''
#normal code

a = int(input("enter a number"))
if a>6:
    print("you have entered a greater number than 6")
    

'''
#using while true
'''
while(True):
    print('press q to quit')
    a = input("enter a number")
    if a=='q':
        break
    a=int(a)
    if a>6:
        print("you have entered a greater number than 6")
print('thanks for playing this game')    '''

#using try
while(True):
    print('press q to quit')
    a = input("enter a number")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("you have entered a greater number than 6")
    except Exception as e:
        print(f"you've entered a wrong input {e}")   
print('thanks for playing this game')    

