
import random

def check_attendence():
    print("Welcome to Employee Wage computation problem")
    # 0 for absent, 1 for full-time, 2 for part-time
    attendence = random.randint(0,2)
    return attendence

def Check_daily_wage():
    wage_per_ht = 20
    wage_attendence = check_attendence()
    if wage_attendence == 1:
        daily_wage = wage_per_ht * 8
        print(f"Employee was present full day so his daily wage is : {daily_wage}")
    elif wage_attendence == 2:
        daily_wage = wage_per_ht * 4
        print(f"Employee was present for half day so his daily wage is : {daily_wage}")
    else:
        daily_wage = 0
        print(f"Employee was absent for the day so his daily wage is : {daily_wage}")
if __name__  == "__main__":
    Check_daily_wage()
