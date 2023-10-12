# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.
import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open(r'C:\edyoda pr\_6_Assignment\employee.json', 'r') as json_file:
    data = json.load(json_file)
    for employee_data in data:
        name = employee_data["name"]
        dob = employee_data["DOB"]
        height = employee_data["height"]
        city = employee_data["city"]
        state = employee_data["state"]
        
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")


# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

indian_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

with open('indian_capitals.json', 'w') as json_file:
    json.dump(indian_capitals, json_file)

print("Data has been written to 'indian_capitals.json' successfully.")
