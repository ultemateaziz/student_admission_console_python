from group import biology, computer


def entry():
        dta = []
        name = input("Enter your name")
        last_name = input("Enter your last name")
        country = input("enter your country:")
        town = input("enter your town")
        for x in [name.lower(), last_name.lower(), country, town]:
            dta.append(x)

        if country.lower() == 'india' and town.lower() == 'mayiladuthurai':
            print("please select your course")
            print("1.Biology")
            print("2.Computer science")

            course = input("select your choice:")

            if course == '1':
                biology(dta)
            elif course == '2':
                computer(dta)
        else:
            print("Your entered value is wrong try again")
            entry()


