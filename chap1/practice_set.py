#1
# wap to open three file 1.txt 2.txt 3.txt if any of there file are not present
# a message without exiting then program must be printed prompting the same

#2 wap to print 3rd 5th and 7th element from a list using enumerate function

# list=[1,3,24,45,12,45,76,8,45,23,23,]
# for i,item in enumerate(list):
#     if i==2 or i==4 or i==6:
#         print(f"the{index+1}th element is {item}")

#3 write a list comprehension to print a list which contains the multiplication table of a user entered number
# num =int(input("entered your number: "))

# table=[num*i for i in range(1,11)]
# print(table)


#4 wap to display a/b where a and b are integers. if b=0,display infinite by handling the zerodivisionerror
# a=int(input("enter your number a: "))
# b=int(input("enter your number b: "))

# try:
#     print(a/b)
# except:
#     print("infinite")   

#5 store the multi[lication tables generated in problem 3 in a file named tables.txt
num =int(input("entered your number: "))

table=[num*i for i in range(1,11)]
print(table)

with open("table.txt","a") as f:
    f.write(str(table))
    f.write('\n')