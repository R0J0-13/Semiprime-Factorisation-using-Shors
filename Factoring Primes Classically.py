#Modules

from math import sqrt
import time
import csv

#Functions

def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

#Variables
N = int()
factors = []
primeFactors = []
time = float()
startTime = float()
endTime = float()

#Main Program

lis = []
with open('rtcClassical.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        lis.append(row)
        
#print(lis)
lst2 = [item[0] for item in lis]

N = int(input("Please enter an Odd Number to factorise: "))

while str(N) in lst2:
    print("This number has already been computed")
    N = int(input("Please enter an Odd Number to factorise: "))

while N % 2 == 0:
    print("The number must be Odd")
    N = int(input("Please enter an Odd Number to factorise: "))

import time 
startTime = time.time()
for number in range (2, N+1):
    if N % number == 0:
        factors.append(number)
    

##print(factors)


for i in range(len(factors)):
    if isPrime(factors[i]) == True:
        primeFactors.append(factors[i])
    else:
        pass

print(primeFactors)
endTime = time.time()
time = endTime - startTime
print(time)

digits = len(str(N))

with open(r'rtcClassical.csv', 'a', newline='') as csvfile:
    fieldnames = ['Number','Digits', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writerow({'Number': str(N), 'Digits': str(digits), 'Time': str(time)})
