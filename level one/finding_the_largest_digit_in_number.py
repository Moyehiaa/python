# finding the largest digit in number
# input your number 
number = input("Enter Your Number : ")    # take input as string
digits = []                               # create empty list to store digits                     
for d in number:                          # iterate through each character in the string
    digits.append(int(d))                 # convert each character to integer and append to list

largest_digit = digits[0]                 # initialize largest digit with the first digit
for c in range(len(digits)):              # iterate through the list of digits
    if (digits[c] > largest_digit):       # compare each digit with the current largest digit
        largest_digit = digits[c]         # update largest digit if current digit is larger
print(largest_digit)                      # print the largest digit