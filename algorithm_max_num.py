#Finding the Largest of Three Numbers with User Input

# Taking three numbers as input from the user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
except ValueError:
    print("Invalid input! Please enter numerical values.")
    exit()

# Comparing them to find the largest number
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num3:
    largest = num2
else:
    largest = num3

# Displaying the largest number
print(f"The largest number is {largest}")