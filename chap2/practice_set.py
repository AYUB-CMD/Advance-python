#1 create two virtual enviroment , install few packages in the first one.
#how do you create  a similar enviroment in the second one?

#2 wap to input name, marks and ph num of a students and format it using the format function like below
#" the name of the students is ayub his marks are 72 and phone number is 98999999"

# name=input("enter your name :")
# marks=input("enter your name :")
# ph=input("enter your phone number :")
# a= "the name of the students is {} his marks are {} and phone number is {}".format(name,marks,ph)
# print(a)

#3 a list contain the multiplication table of 7.
# wap to convert it to a vertical string of a same number

# l=[str(i*7) for i in range(1,11)]
# print(l)

# ver="\n".join(l)
# print(ver)


#4 wap to filter a list of number whisch are divisible by 5

# l=[34,55,25,35,44,22,20]
# div=lambda a: a%5==0
# print(list(filter(div, l)))

#5 wap to find the max of the num in a list using the reduce function
# from functools import reduce


# l=[1,2,3,4,6,7,4]

# a=reduce(max, l)
# print(a)

#6 run pip freeze for the system interpretor . take the content ans create a virtualenv



#7 explore the flask module and create a web server using flask and python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" crossorigin="anonymous"></script>
    -->
  </body>
</html>'''
if __name__ =="__main__" :
    app.run(debug=True)   

