total = {
            'employee' : 0,
            'hours' : 0,
            'tax' : 0,
            'net' : 0
          }

all_employee_name = []
all_total_hours = []
all_hourly_rate = []
all_income_tax_rate = []
all_income_tax = []
all_net_pay = []
all_to_date = []
all_from_date = []
all_gross_pay = []



def get_employee_name():
    employee_name = input("Input employee name: ")
    return employee_name

def get_total_hours():
    total_hours = int(input("Input total hours : "))
    return total_hours

def get_hourly_rate():
    hourly_rate = int(input("Input Hourly rate : "))
    return hourly_rate

def get_income_tax_rate():
    tax_rate = int(input("Input income tax rate: "))
    return tax_rate

def get_net_pay(total_hours, hourly_rate, income_tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * income_tax_rate / 100
    net_pay = gross_pay - income_tax
    return income_tax, net_pay, gross_pay

def display_employee(employee_name, total_hours, hourly_rate, income_tax_rate, income_tax, net_pay, gross_pay, from_day, to_day):
    print("Employee Name : ", employee_name)
    print("Total Hours : ", total_hours)
    print("Hourly Rate : ", hourly_rate)
    print("Income Tax Rate : ", income_tax_rate)
    print("Income tax : ", income_tax)
    print("Income net : ", net_pay)
    print("Gross pay : ", gross_pay)
    print("From day : ", from_day)
    print("To day : ", to_day)

def display_all_employee():
    print(f"Total Employee : {total_employee}")
    print(f"Total Hours : {total_employee_hours}")
    print(f"Total Tax : {total_employee_tax}")
    print(f"Total Net Pay : {total_employee_net_pay}")

def get_date():
    from_date = ''
    to_date = ''
    from_date = input("input from date: ")
    if(from_date == "End."):
        return from_date, to_date
    to_date = input("input to date: ")
    return from_date, to_date




while True:
    from_date, to_date = get_date()
    if(from_date == "End."):
        break
    all_from_date.append(from_date)
    all_to_date.append(to_date)
    employee_name = get_employee_name()
    all_employee_name.append(employee_name)
    total_hours = get_total_hours()
    all_total_hours.append(total_hours)
    hourly_rate = get_hourly_rate()
    all_hourly_rate.append(hourly_rate)
    income_tax_rate = get_income_tax_rate()
    all_income_tax_rate.append(income_tax_rate)
    income_tax, net_pay, gross_pay = get_net_pay(total_hours, hourly_rate, income_tax_rate)
    all_income_tax.append(income_tax)
    all_net_pay.append(net_pay)
    all_gross_pay.append(gross_pay)

# when the loop is terminated

for i in range(len(all_employee_name)):
    display_employee(all_employee_name[i], all_total_hours[i], all_hourly_rate[i], all_income_tax_rate[i], all_income_tax[i], all_net_pay[i], all_gross_pay[i], all_from_date[i], all_to_date[i])
    total['employee'] += 1
    total['hours'] += all_total_hours[i]
    total['tax'] += all_income_tax[i]
    total['net'] += all_net_pay[i]


print("Total Employee : {}".format(total['employee']))
print("Total Hours : {}".format(total['hours']))
print("Total Income Tax : {}".format(total['tax']))
print("Total Net Pay : {}".format(total['net']))



