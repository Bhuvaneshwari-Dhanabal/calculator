🧮 Python Multi-Input Calculator

(Project Documentation)

📘 Overview

The Python Multi-Input Calculator is a command-line tool that allows users to perform arithmetic operations — addition, subtraction, multiplication, and division — on multiple numbers at once.

Unlike a basic calculator that only handles two numbers, this calculator lets users decide how many numbers they want to input and performs the operation on all of them sequentially.

This project demonstrates the use of functions, loops, recursion, and error handling in Python.

🎯 Project Objective

To create a flexible, interactive, and error-resistant calculator that:

Accepts any number of inputs

Allows the user to select an operation

Handles invalid input gracefully

Lets the user run multiple calculations in one session

⚙️ How It Works

The program begins by printing a title:

print("Python Multi-Input Calculator")


It asks the user:

How many numbers do you want to use?


If the user enters less than 2, it restarts automatically.

It collects all the numbers using a loop and validates each one using the check() function.

for i in range(count):
    num = input(f"Enter number {i + 1}: ")
    if check(num):
        numbers.append(int(num))


The user chooses an operation:

Choose operation (*, /, +, -):


Based on the selected operation, the program calculates the result using a loop:

for n in numbers[1:]:
    if operation == "+":
        result += n
    elif operation == "-":
        result -= n
    elif operation == "*":
        result *= n
    elif operation == "/":
        result /= n


It then prints the final result:

The result of your calculation is: <result>


Finally, the user is asked whether to run again or exit:

Would you like to use the calculator again? (y/n)

🧩 Functions Explanation
Function	Description
calculator()	Handles the entire logic for taking inputs, validating numbers, performing operations, and displaying the result.
check(possibleInt)	Verifies if the input is a valid integer. Returns True or False.
again()	Asks the user if they want to perform another calculation. If “yes”, restarts the program; otherwise exits.
main()	Controls the overall flow — starts calculator, then checks if user wants to continue.
💡 Features

✅ Accepts any number of inputs (2 or more)
✅ Supports four operations: addition, subtraction, multiplication, division
✅ Handles invalid inputs and errors gracefully
✅ Uses recursion for repeating operations smoothly
✅ Friendly, beginner-friendly interface

🧠 Error Handling

If the user enters text instead of a number → shows a message and restarts.

If the user enters fewer than 2 numbers → prompts again.

If division by zero occurs → prints an error message and restarts.

If the user types an invalid operation → prompts again.

🖥️ Example Run
Python Multi-Input Calculator
How many numbers do you want to use? 3
Enter number 1: 5
Enter number 2: 10
Enter number 3: 2
Choose operation (*, /, +, -): *
The result of your calculation is: 100

Would you like to use the calculator again? (y/n): y
