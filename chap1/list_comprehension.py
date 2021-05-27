a = [3,4,56,7,8,22,55,67,989,00,34,344,565,87,43,44,66,778,8]
b=[]

# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

b=[i for i in a if i%2==0]
print(b)

# set comprehension
t =[1,2,4,2,4,1,2,3]
s= {i for i in t}
print(s)