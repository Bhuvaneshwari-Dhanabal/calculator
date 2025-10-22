print("Python Multi-Input Calculator")
def calculator():
    try:
        count = int(input("How many numbers do you want to use? "))
        if count < 2:
            print("You must enter at least two numbers.\n")
            calculator()
            return

        numbers = []
        for i in range(count):
            num = input(f"Enter number {i + 1}: ")
            if check(num):
                numbers.append(int(num))
            else:
                print("Invalid number. Try again.")
                return calculator()

        operation = input("Choose operation (*, /, +, -): ").strip()

        if operation not in ["*", "/", "+", "-"]:
            print("Invalid operation! Please choose one of *, /, +, -.\n")
            return calculator()

        result = numbers[0]

        for n in numbers[1:]:
            if operation == "+":
                result += n
            elif operation == "-":
                result -= n
            elif operation == "*":
                result *= n
            elif operation == "/":
                    print("Error: Division by zero not allowed.")
                    return calculator()
                result /= n

        print(f"\nThe result of your calculation is: {result}\n")

    except ValueError:
        print("Please enter a valid number for count.\n")
        calculator()

def check(possibleInt):
    try:
        int(possibleInt)
        return True
    except ValueError:
        return False

def again():
    repeat = input("Would you like to use the calculator again? (y/n): ").lower()
    if repeat in ["y", "yes"]:
        main()
    elif repeat in ["n", "no"]:
        print("Goodbye!")
        quit()
    else:
        print("Invalid input.\n")
        again()

def main():
    calculator()
    again()

main()
