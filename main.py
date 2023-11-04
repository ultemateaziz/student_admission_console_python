import studentEntry
import studentLogin
import adminLogin

def start():
    print("1.Student Login")
    print("2.Teacher Login")
    print("3.Student Registration")
    ans = input("Enter your choice :")
    if ans == '3':
        studentEntry.entry()
    elif ans == '1':
        studentLogin.stdLog()
    elif ans == '2':
        adminLogin.adminLog()


start()
