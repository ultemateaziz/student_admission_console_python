from fileHandling import file

def checker(percentage, dta, marks):

    if percentage >= 60:
        print("Your selected")
        file(percentage, dta, marks)
    else:
        print("your not selected")

