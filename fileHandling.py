import os

def file(percentage, dta, marks):
    path = 'studentdetails.txt'

    if(os.path.exists(path)):
        print("file already exist")
    else:
        file = open(path ,'x')

    file = open(path,'a')
    file.write("\n")
    for i in dta:
        file.write(i)
        file.write('\t')
    for i in marks:
        file.write(i)
        file.write('\t')

    file.write(str(percentage))
