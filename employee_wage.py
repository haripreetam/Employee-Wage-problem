import random

def check_attendance():
    #print("Welcome to Employee Wage computation problem")
    # 0 for absent, 1 for full-time, 2 for part-time
    attendance = random.randint(0, 2)
    return attendance

def calculate_Full_Day_Wage(wage_per_ht):
    return wage_per_ht * 8, 8

def calculate_Half_Day_Wage(wage_per_ht):
    return wage_per_ht * 4, 4

def calculate_Absent_Wage(wage_per_ht):
    return 0 ,0

def calculate_daily_wage():
    wage_per_ht = 20
    attendance = check_attendance()
    
    # Dictionary to simulate switch-case
    switcher = {
        1: calculate_Full_Day_Wage,
        2: calculate_Half_Day_Wage,
        0: calculate_Absent_Wage
    }

    # Get the function from switcher dictionary
    func = switcher.get(attendance, lambda wage_per_ht:0)
    
    # Execute the function
    return func(wage_per_ht)

def cal_monthly_wage():
    total_wage = 0
    total_hours = 0
    total_days = 0
    max_hours = 100
    max_days = 20
    
    while total_hours < max_hours and total_days < max_days:
        daily_wage, hours_worked = calculate_daily_wage()#getting the tuples
        total_wage += daily_wage
        total_hours += hours_worked
        total_days += 1
    
    return total_wage


if __name__ == "__main__":
    monthly_wage = cal_monthly_wage()
    print(f"Monthly wage of the employee is: {monthly_wage}")

