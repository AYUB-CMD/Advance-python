def read(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file not found {filename}")

read("chap1\one.txt")
read("two.txt")
#read("chap1\two.txt")