
# This program finds the largest digit in a given number.
# It prompts the user to enter a number and then iterates through each digit
# to determine the largest one.

number = input("Enter your number to find the largest digit: ")
largest = int(number[0])       # Initialize largest with the first digit.
for digit in number:           # Iterate through each digit in the number.
    if int(digit) > largest:   # If the current digit is greater than the current largest, update largest.
        largest = int(digit)
print("The largest digit in the number is:", largest) # Print the largest digit.