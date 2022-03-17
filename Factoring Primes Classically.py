#Modules

from math import sqrt #Imports the sqrt package from the math Library Module from Python's Library Directory 
import time #Imports the time Library Module from Python's Library Directory 
import csv #Imports the csv Library Module from Python's Library Directory 

#Functions

def isPrime(n):
 
    # Corner case
    if (n <= 1): #Condition to check whether entered number is less than 1
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1): 
        if (n % i == 0): #Condition to check if there is a remainder
            return False
 
    return True

#Variables
N = int() #An Integer to store the number to be factored
factors = [] #A List to store all the factors of the entered number
primeFactors = [] #A List to store just the prime factors of the entered number
time = float() #A Real number to store the execution time of the algorithm
startTime = float() #A Real number to mark the starting time of the algorithm
endTime = float() #A Real number to mark the ending time of the algorithm

#Main Program

lis = [] #A List to store the elements retrieved from the csv file
with open('rtcClassical.csv', 'r') as file: #Opens the csv file named rtcClassical in Read mode
    reader = csv.reader(file) #Collates all elements of the file to a variable
    for row in reader: #Parses the file elements 
##        print(row) #FOR TESTING PURPOSES
        lis.append(row) #Adds each row of the csv file to a list
        
##print(lis) #FOR TESTING PURPOSES
lst2 = [item[0] for item in lis] #Extracts the elements in the first column of the csv file into a list

N = int(input("Please enter an Odd Number to factorise: ")) #User Input to get a number to be factorised

while str(N) in lst2: #A check to ensure already factorised numbers are not repeated
    print("This number has already been computed")
    N = int(input("Please enter an Odd Number to factorise: "))

while N % 2 == 0: #A check to ensure the entered number is odd
    print("The number must be Odd")
    N = int(input("Please enter an Odd Number to factorise: "))

import time 
startTime = time.time() #A marker to denote the beginning of the time measurement
for number in range (2, N+1): #Iterates from 2 to till one more than the user input
    if N % number == 0: #Condition to check the user input yields a remainder with the number element
        factors.append(number) #Adds the number element to the factors list
    

##print(factors) #FOR TESTING PURPOSES ONLY


for i in range(len(factors)): #Iteration over the factors list
    if isPrime(factors[i]) == True: #Condition to check whether the factors are prime 
        primeFactors.append(factors[i]) #Adds the prime factors to the primeFactors list
    else:
        pass

print(primeFactors) #Outputs the prime factors of the user input onto the screen
endTime = time.time() #A marker to denote the end of the time measurement
time = endTime - startTime #The execution time is determined
print(time) #Outputs the execution time onto the screen

digits = len(str(N)) #Stores the number of digits in the inputted number

with open(r'rtcClassical.csv', 'a', newline='') as csvfile: #Opens the csv file named rtcClassical in Append mode
    fieldnames = ['Number','Digits', 'Time'] #Stores the row heading names
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames) #Creates the row headings for the csv file

    writer.writerow({'Number': str(N), 'Digits': str(digits), 'Time': str(time)}) #Writes to the csv file in the respective fields
