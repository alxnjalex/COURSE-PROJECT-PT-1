total_employee = 0
total_employee_hours = 0
total_employee_gross_pay = 0
total_employee_tax = 0
total_employee_net_pay = 0



def get_employee_name():
    global total_employee
    employee_name = input("Input employee name: ")
    total_employee += 1
    return employee_name

def get_total_hours():
    global total_employee_hours
    total_hours = int(input("Input total hours : "))
    total_employee_hours += total_hours
    return total_hours

def get_hourly_rate():
    hourly_rate = int(input("Input Hourly rate : "))
    return hourly_rate

def get_income_tax_rate():
    tax_rate = int(input("Input income tax rate: "))
    return tax_rate

def get_net_pay(total_hours, hourly_rate, income_tax_rate):
    global total_employee_tax
    global total_employee_net_pay
    global total_employee_gross_pay
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * income_tax_rate / 100
    net_pay = gross_pay - income_tax
    total_employee_gross_pay += gross_pay
    total_employee_tax += income_tax
    total_employee_net_pay += net_pay
    return income_tax, net_pay

def display_employee(employee_name, total_hours, hourly_rate, income_tax_rate, income_tax, net_pay):
    print("Employee Name : ", employee_name)
    print("Total Hours : ", total_hours)
    print("Hourly Rate : ", hourly_rate)
    print("Income Tax Rate : ", income_tax_rate)
    print("Income tax : ", income_tax)
    print("Income net : ", net_pay)


def display_all_employee():
    print(f"total employee : {total_employee}")
    print(f"total hours : {total_employee_hours}")
    print(f"total tax : {total_employee_tax}")
    print(f"total net pay : {total_employee_net_pay}")




while True:
    employee_name = get_employee_name()
    if(employee_name == "End."):
        break;
    total_hours = get_total_hours()
    hourly_rate = get_hourly_rate()
    income_tax_rate = get_income_tax_rate()
    income_tax, net_pay = get_net_pay(total_hours, hourly_rate, income_tax_rate)
    display_employee(employee_name, total_hours, hourly_rate, income_tax_rate, income_tax, net_pay)
    display_all_employee()

