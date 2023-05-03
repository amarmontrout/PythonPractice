def pick_number():
    while True:
        num = int(input("Please enter a whole number greater than 1: "))
        if num < 1:
            print("Number must be greater than 1. ")
        elif num > 1:
            return num
        else:
            print("Number can't be 1. ")


def count_down(num):
    while num != -1:
        print(num)
        num = num - 1


def factorial(count):
    num = 1
    for i in range(1, count + 1):
        num = num * i
    print(num)


while True:
    number = pick_number()
    choice = int(input("Type 1 to countdown or 2 to display the factorial. (Type 0 to exit): "))
    if choice == 1:
        count_down(number)
    elif choice == 2:
        factorial(number)
    elif choice == 0:
        break
    else:
        print("Invalid choice. Start over.")
print("Goodbye.")
