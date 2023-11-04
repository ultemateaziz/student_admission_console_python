
def stdLog():
    file = open('studentdetails.txt', 'r')
    username = input("enter your username:")
    password = input("enter your password:")

    a = file.read()
    dta = a.split()
    if username.lower() in dta:
        print("your data is registered:")
    else:
        print("not registered")

