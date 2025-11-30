# this program will take a number from user and print all the prime numbers until that number.



# function is_prime to check if a number is prime or not


def is_prime(n):                             # check if n is less than or equal to 1.
    if(n <= 1):
        return False                         # if n is greater than 1 then it is not prime.
    for i in range(2,int(n**0.5)+1):         # check for factors from 2 to the square root of n.
        if(n % i == 0):
            return False                     # if n is divisible by any number in this range, it is not prime.
    else :  
        return True                          # if n is not divisible by any number in this range, it is prime. 

prime_list = []                              # empty list to store prime numbers
number = input("Enter your limit number to see all the prime numbers : ")   # take input from user
digit = int(number)                          # convert input to integer
for i in range(1, digit +1):                 # iterate from 1 to the input number
    if is_prime(i):                          # check if the number is prime
        prime_list.append(i)                 # append prime numbers to the list
print(prime_list)                            # print the list of prime numbers