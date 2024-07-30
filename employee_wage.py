import random

class Employee:
    # wage_per_ht = 20
    # max_hours = 100
    # max_days = 20
    
    def __init__(self):
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
    
    @classmethod
    def check_attendance(cls):
        # 0 for absent, 1 for full-time, 2 for part-time
        return random.randint(0, 2)
    
    @classmethod
    def calculate_full_day_wage(cls, wage_per_hour):
        return wage_per_hour * 8, 8
    
    @classmethod
    def calculate_half_day_wage(cls, wage_per_hour):
        return wage_per_hour * 4, 4
    
    @classmethod
    def calculate_absent_wage(cls, wage_per_hour):
        return 0, 0
    
    @classmethod
    def calculate_daily_wage(cls, wage_per_hour):
        attendance = cls.check_attendance()
        
        switcher = {
            1: cls.calculate_full_day_wage,
            2: cls.calculate_half_day_wage,
            0: cls.calculate_absent_wage
        }
        func = switcher.get(attendance, lambda wage_per_hour: (0, 0))
        
        return func(wage_per_hour)
    
    def cal_monthly_wage(self, wage_per_hour, max_hours, max_days):
        while self.total_hours < max_hours and self.total_days < max_days:
            daily_wage, hours_worked = Employee.calculate_daily_wage(wage_per_hour)
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1
        
        return self.total_wage

class Company:
    def __init__(self, name, wage_per_hour, max_hours, max_days):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.max_hours = max_hours
        self.max_days = max_days
        self.employee = Employee()
    
    def calculate_employee_wage(self):
        return self.employee.cal_monthly_wage(self.wage_per_hour, self.max_hours, self.max_days)
    
if __name__ == "__main__":
    companies = [
        Company("CompanyA", 20, 100, 20),
        Company("CompanyB", 25, 120, 22),
        Company("CompanyC", 30, 110, 21)
    ]
    
    for company in companies:
        monthly_wage = company.calculate_employee_wage()
        print(f"Monthly wage for an employee in {company.name} is: {monthly_wage}")
