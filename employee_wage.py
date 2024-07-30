import random

class Employee:
    wage_per_ht = 20
    max_hours = 100
    max_days = 20
    
    def __init__(self):
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
    
    @classmethod
    def check_attendance(cls):
        # 0 for absent, 1 for full-time, 2 for part-time
        return random.randint(0, 2)
    
    @classmethod
    def Calculate_Full_Day_Wage(cls):
        return cls.wage_per_ht * 8, 8
    
    @classmethod
    def Calculate_Half_Day_Wage(cls):
        return cls.wage_per_ht * 4, 4
    
    @classmethod
    def Calculate_Absent_Wage(cls):
        return 0, 0
    
    @classmethod
    def Calculate_Daily_Wage(cls):
        attendance = cls.check_attendance()
        
        # Dictionary to simulate switch-case
        switcher = {
            1: cls.Calculate_Full_Day_Wage,
            2: cls.Calculate_Half_Day_Wage,
            0: cls.Calculate_Absent_Wage
        }

        # Get the function from switcher dictionary
        func = switcher.get(attendance, lambda: (0, 0))
        
        # Execute the function
        return func()
    
    def cal_monthly_wage(self):
        while self.total_hours < Employee.max_hours and self.total_days < Employee.max_days:
            daily_wage, hours_worked = Employee.Calculate_Daily_Wage()
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1
        
        return self.total_wage

if __name__ == "__main__":
    emp = Employee()
    monthly_wage = emp.cal_monthly_wage()
    print(f"Monthly wage of the employee is: {monthly_wage}")
