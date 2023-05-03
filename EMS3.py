names = []
ssns = []
phone_numbers = []
emails = []
salaries = []
num_emp = 0


def add_emp():
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


def view_emp():
    print("There are (" + str(num_emp) + ") employees in the system.")
    print("They are the following employees:")
    for emp_names in names:
        print(emp_names)


while True:
    choice = input("Type 1 to add employee. Type 2 to view employees. Type done to exit.\n")
    if choice == "1":
        add_emp()
        num_emp += 1
    elif choice == "2":
        view_emp()
    elif choice.lower() == "done":
        break
    else:
        print("Invalid input.")
input("Goodbye.")
