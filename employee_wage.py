import random

def check_attendance():
    print("Welcome to Employee Wage computation problem")
    # 0 for absent, 1 for full-time, 2 for part-time
    attendance = random.randint(0, 2)
    return attendance

def calculate_Full_Day_Wage(wage_per_ht):
    daily_wage = wage_per_ht * 8
    print(f"Employee was present full day so his daily wage is: {daily_wage}")

def calculate_Half_Day_Wage(wage_per_ht):
    daily_wage = wage_per_ht * 4
    print(f"Employee was present for half day so his daily wage is: {daily_wage}")

def calculate_Absent_Wage(wage_per_ht):
    daily_wage = 0
    print(f"Employee was absent for the day so his daily wage is: {daily_wage}")

def check_daily_wage():
    wage_per_ht = 20
    attendance = check_attendance()
    
    # Dictionary to simulate switch-case
    switcher = {
        1: calculate_Full_Day_Wage,
        2: calculate_Half_Day_Wage,
        0: calculate_Absent_Wage
    }

    # Get the function from switcher dictionary
    func = switcher.get(attendance, lambda wage_per_ht: print("Invalid attendance status"))
    
    # Execute the function
    func(wage_per_ht)

if __name__ == "__main__":
    check_daily_wage()

