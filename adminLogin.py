def adminLog():
    username = input("Enter your username :")
    password = input("Enter your password:")

    if (username == 'admin' and password == 'computer'):
        file = open('studentdetails.txt', 'r')
        data = file.read().split()
        i = 0
        while (i < len(data)):
            print(data[i])
            i += 13
