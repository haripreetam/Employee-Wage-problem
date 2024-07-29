
import random

def check_attendence():
    attendence = random.randint(0,1)
    if attendence == 1:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__  == "__main__":
    print("Welcome to Employee Wage Program")
    check_attendence()
