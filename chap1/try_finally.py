#try except finally
try:
    i=int(input('enter a number'))
    c=1/i
except Exception as e:
    print(e) 
    exit()
finally:
    print("finally we're done")
print("if you've entered wrong input or error it wont print")    