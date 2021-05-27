a=56#global var
def func1():
    global a
    print(a)
    a=5 #local var
    print(a)

func1()
print(a)#global var is changed in func1() with local var