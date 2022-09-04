user_ids = []
user_pass = []
auth_code = []

def login():

    #open text file with the user login information
    with open("user.txt", "r+", newline='') as file:

        # read each record and store in a list
        for line in file:
            record = line.split('|')
            user_ids.append(record[0])
            user_pass.append(record[1])
            auth_code.append(record[2])
    file.close()

    user_id = input("Input your user ID : ")
    user_password = input("Input your user password : ")
    user_code = ''
    for idx, id in enumerate(user_ids):
        if(id == user_id and user_password == user_pass[idx]):
            user_code = auth_code[idx][:-2] #grabing the authorization code except the newline

    return user_id, user_code


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


def get_date():
    from_date = ''
    to_date = ''
    from_date = input("input from date: ")
    if (from_date == "End."):
        return from_date, to_date
    to_date = input("input to date: ")
    return from_date, to_date


def get_from_date(filename, id, code):
    total = {
        'employee': 0,
        'hours': 0,
        'tax': 0,
        'net_pay': 0,
    }
    with open(filename, "r") as f:
        from_date = input("From Date : ")
        print(f"User ID = {id}, Authentication Code : {code}")
        if (from_date == "All"):
            for line in f:
                words = line.split('|')
                print("Employee Name : ", words[2])
                print("Total Hours : ", words[3])
                print("Hourly Rate : ", words[4])
                print("Income Tax Rate : ", words[5])
                print("Income tax : ", words[6])
                print("Income net : ", words[7])
                print("Gross pay : ", words[8])
                print("From day : ", words[0])
                print("To day : ", words[1])

                total['employee'] += 1
                total['hours'] += int(float(words[3]))
                total['tax'] += int(float(words[6]))
                total['net_pay'] += int(float(words[7]))
        else:
            for line in f:
                words = line.split('|')
                if words[0] == from_date:
                    print("Employee Name : ", words[2])
                    print("Total Hours : ", words[3])
                    print("Hourly Rate : ", words[4])
                    print("Income Tax Rate : ", words[5])
                    print("Income tax : ", words[6])
                    print("Income net : ", words[7])
                    print("Gross pay : ", words[8])
                    print("From day : ", words[0])
                    print("To day : ", words[1])

                    total['employee'] += 1
                    total['hours'] += int(float(words[3]))
                    total['tax'] += int(float(words[6]))
                    total['net_pay'] += int(float(words[7]))

        print("Total Employee = ", total["employee"])
        print("Total Hours = ", total["hours"])
        print("Total Tax = ", total["tax"])
        print("Total Net Pay = ", total["net_pay"])


filename = "employee.txt"
id, code = login()
if(code == ''):
    print("User ID or Password is Wrong")

elif(code == 'Admin'):
    with open(filename, "a") as f:
        while True:
            from_date, to_date = get_date()
            if (from_date == "End."):
                break
            f.write(from_date)  # 0
            f.write('|')
            f.write(to_date)  # 1
            f.write('|')
            employee_name = get_employee_name()
            f.write(employee_name)  # 2
            f.write('|')
            total_hours = get_total_hours()
            f.write(str(total_hours))  # 3
            f.write('|')
            hourly_rate = get_hourly_rate()
            f.write(str(hourly_rate))  # 4
            f.write('|')
            income_tax_rate = get_income_tax_rate()
            f.write(str(income_tax_rate))  # 5
            f.write('|')
            income_tax, net_pay, gross_pay = get_net_pay(total_hours, hourly_rate, income_tax_rate)
            f.write(str(income_tax))  # 6
            f.write('|')
            f.write(str(net_pay))  # 7
            f.write('|')
            f.write(str(gross_pay))  # 8
            f.write('\n')
    get_from_date(filename, id, code)
else:
    get_from_date(filename, id, code)
