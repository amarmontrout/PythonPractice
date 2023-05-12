import os
names = []
ssns = []
phone_numbers = []
emails = []
salaries = []
num_emp = 0


def add_emp():
    print("-----ADD NEW EMPLOYEE-----")
    print()
    print("Enter information for employee " + str(len(names) + 1))
    name = str(input("Enter employee name: "))
    ssn = str(input("Enter employee SSN: "))
    phone = str(input("Enter employee phone number (xxx) xxx-xxxx: "))
    email = str(input("Enter employee email: "))
    salary = str(input("Enter employee salary: "))
    names.append(name)
    ssns.append(ssn)
    phone_numbers.append(phone)
    emails.append(email)
    salaries.append(salary)
    os.system('cls')


def view_emp():
    if num_emp > 0:
        print("-----VIEW ALL EMPLOYEES-----")
        print()
        index = 0
        while True:
            if index < len(names):
                print("----------", names[index], "----------")
                print("SSN: " + ssns[index])
                print("Phone: " + phone_numbers[index])
                print("Email: " + emails[index])
                print("Salary: $" + salaries[index])
                print("------------------------------")
                print()
                index += 1
            else:
                break
        input("Press enter to continue")
        os.system('cls')
    if num_emp == 0:
        print("There are no employees in the system.")
        input("Press enter to continue")
        os.system('cls')


def search_ssn():
    while True:
        print("-----SSN EMPLOYEE SEARCH-----")
        print()
        ss_num = input("Please enter employee SSN (Type done to exit): ")
        os.system('cls')
        if ss_num in ssns:
            index = ssns.index(ss_num)
            print("-----SSN EMPLOYEE SEARCH-----")
            print()
            print("----------", names[index], "----------")
            print("SSN: " + ssns[index])
            print("Phone: " + phone_numbers[index])
            print("Email: " + emails[index])
            print("Salary: $" + salaries[index])
            print("------------------------------")
            print()
            input("Press enter to continue")
            os.system('cls')
        elif ss_num.lower() == "done":
            return
        else:
            print("Invalid SSN.")


def edit_emp():
    while True:
        print("-----EDITING EMPLOYEE INFORMATION-----")
        print()
        ss_num = input("Please enter employee SSN (Type done to exit): ")
        os.system('cls')
        if ss_num in ssns:
            while True:
                index = ssns.index(ss_num)
                print("-----EDITING EMPLOYEE INFORMATION-----")
                print()
                print("----------", names[index], "----------")
                print("SSN: " + ssns[index])
                print("Phone: " + phone_numbers[index])
                print("Email: " + emails[index])
                print("Salary: $" + salaries[index])
                print("------------------------------")
                print()
                print('1:Edit name\n2:Edit SSN\n3:Edit phone number\n4:Edit email\n5:Edit salary\n0:Exit\n')
                edit_choice = int(input("Please enter your option: "))
                if edit_choice == 1:
                    new_name = input("Enter new name: ")
                    names[index] = new_name
                    os.system('cls')
                elif edit_choice == 2:
                    new_ssn = input("Enter new SSN: ")
                    ssns[index] = new_ssn
                    ss_num = new_ssn
                    os.system('cls')
                elif edit_choice == 3:
                    new_phone = input("Enter new phone number (xxx) xxx-xxxx: ")
                    phone_numbers[index] = new_phone
                    os.system('cls')
                elif edit_choice == 4:
                    new_email = input("Enter new email: ")
                    emails[index] = new_email
                    os.system('cls')
                elif edit_choice == 5:
                    new_salary = input("Enter new salary: ")
                    salaries[index] = new_salary
                    os.system('cls')
                elif edit_choice == 0:
                    os.system('cls')
                    return
                else:
                    print("Invalid choice.")
        elif ss_num.lower() == 'done':
            break
        else:
            print("Employee not found.")


def exp_emp():
    with open("employees.txt", "w") as emp_file:
        for i in range(len(names)):
            emp_file.write(f"{names[i]},{ssns[i]},{phone_numbers[i]},{emails[i]},{salaries[i]}\n")
        print("--------EXPORT SUCCESSFUL----------")
        print()
        input("Press enter to continue")
        os.system('cls')


def imp_emp():
    global num_emp
    with open("employees.txt", "r") as emp_file:
        for line in emp_file:
            information = line.strip().split(',')
            names.append(information[0])
            ssns.append(information[1])
            phone_numbers.append(information[2])
            emails.append(information[3])
            salaries.append(information[4])
            num_emp += 1


while True:
    print("------------Employee Management System------------")
    print(f"There are ({num_emp}) employees in the system.")
    print("--------------------------------------------------")
    print("1. Add new employee\n2. View all employees\n3. Search employee by SSN\n4. Edit employee information")
    print("5. Export employees' information into a text file\n6. Import employees' information from a text file")
    print("--------------------------------------------------")
    choice = int(input("Please enter your option number: "))
    if choice == 1:
        os.system('cls')
        add_emp()
        num_emp += 1
    elif choice == 2:
        os.system('cls')
        view_emp()
    elif choice == 3:
        os.system('cls')
        search_ssn()
    elif choice == 4:
        os.system('cls')
        edit_emp()
    elif choice == 5:
        os.system('cls')
        exp_emp()
    elif choice == 6:
        os.system('cls')
        imp_emp()
    else:
        os.system('cls')
        print("Invalid input.")
