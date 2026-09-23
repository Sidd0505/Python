class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, age, hours_worked, hourly_rate):
        super().__init__(name, age)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

# Creating instances of FullTimeEmployee and PartTimeEmployee
full_time_emp = FullTimeEmployee("Alice", 35, 5000)
part_time_emp = PartTimeEmployee("Bob", 25, 20, 15)

# Calculating salary for both employees
full_time_salary = full_time_emp.calculate_salary()
part_time_salary = part_time_emp.calculate_salary()

print(f"{full_time_emp.name}'s salary: ${full_time_salary}")
print(f"{part_time_emp.name}'s salary: ${part_time_salary}")


#########output##########
Alice's salary: $5000
Bob's salary: $300
