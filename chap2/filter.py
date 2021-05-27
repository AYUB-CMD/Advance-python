def greater_than_5(num):
    if num>5:
        return True
    else:
        return False  

l=[1,4,5,6,7,8,8,9,4,324,6,56,7]    

print(list(filter(greater_than_5, l)))