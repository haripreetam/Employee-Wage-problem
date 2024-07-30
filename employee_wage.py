
import random

def check_attendence():
    print("Welcome to Employee Wage computation problem")
    attendence = random.randint(0,1)
    return attendence

def Check_daily_wage():
    wage_per_ht = 20
    wage_attendence = check_attendence()
    if wage_attendence == 1:
        daily_wage = wage_per_ht * 8
        print(f"Employee was present full day so his daily wage is : {daily_wage}")
    else:
        daily_wage = 0
        print(f"Employee was absent for the day so his daily wage is : {daily_wage}")
if __name__  == "__main__":
    Check_daily_wage()
