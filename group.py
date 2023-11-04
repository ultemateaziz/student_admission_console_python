from percentageChecker import checker

marks = []


def biology(dta):
    eng = int(input("Enter marks english"))
    tam = int(input("Enter marks tamil"))
    mat = int(input("Enter marks maths"))
    phy = int(input("Enter marks phy"))
    che = int(input("Enter marks che"))
    bio = int(input("Enter marks bio"))
    if eng>=35 and tam>=35 and mat>=35 and phy>=35 and che>=35 and bio>=35:
        tot = eng + tam + mat + phy + che + bio
        percentage = tot / 6
        print("Your total mark is:", tot, "your percentage is:", percentage)
        for i in [eng, tam, mat, phy, che, bio]:
            marks.append(str(i))
        checker(percentage, dta, marks)
    else:
        print("Your enter low level marks try your next exam")

def computer(dta):
    eng = int(input("Enter marks english"))
    tam = int(input("Enter marks tamil"))
    mat = int(input("Enter marks maths"))
    phy = int(input("Enter marks phy"))
    che = int(input("Enter marks che"))
    cs = int(input("Enter marks cs"))

    if eng>=35 and tam>=35 and mat>=35 and phy>=35 and che>=35 and cs>=35:
        tot = eng + tam + mat + phy + che + cs
        percentage = tot / 6
        print("Your total mark is:", tot, "your percentage is:", percentage)
        for i in [eng, tam, mat, phy, che, cs]:
            marks.append(str(i))
        checker(percentage, dta, marks)
    else:
        print("your entered low level marks try next exam")
