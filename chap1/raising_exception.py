def incre(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not good")  

a =incre(95) 
print(a)         