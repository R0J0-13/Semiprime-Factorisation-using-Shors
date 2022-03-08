"~~~~~~~~~~Modules~~~~~~~~~~"

from qiskit import IBMQ
from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor
import csv
import time

"~~~~~~~~~~Readying the Quantum Computer for Processing~~~~~~~~~~"

IBMQ.enable_account("89f61d6c1b19c9d71fd0652f9cec6f8b007434be6a70da5f8a0f98bfece0aed9b26c2de968a0adab84a664f14213dfcf33579a5f385f264f41be4059c54f4d3e") # Enter your API token here
provider = IBMQ.get_provider(hub = "ibm-q")

#backend = provider.get_backend('ibmq_qasm_simulator') # Specifies the quantum device
backend = Aer.get_backend("qasm_simulator")
#backend = provider.get_backend('ibmq_vigo') # Specifies the quantum device

"~~~~~~~~~~Variables~~~~~~~~~~"

"~~~~~~~~~~Main~~~~~~~~~~"

lis = []
with open('rtcQuantum.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        lis.append(row)
        
#print(lis)
lst2 = [item[0] for item in lis]

userInput = int(input("Please enter an Odd Number to factorise: "))

while str(userInput) in lst2:
    print("This number has already been computed")
    userInput = int(input("Please enter an Odd Number to factorise: "))

while userInput % 2 == 0:
    print("The number must be Odd")
    userInput = int(input("Please enter an Odd Number to factorise: "))


print("\n Shors Algorithm")
print("--------------------")
print("\nExecuting...\n")    

import time 
startTime = time.time()
  
N = Shor(userInput) #Function to run Shor's algorithm where 21 is the integer to be factored

result_dict = N.run(QuantumInstance(backend, shots = 1, skip_qobj_validation = False))
primeFactors = result_dict["factors"] # Get factors from results

print(primeFactors)

endTime = time.time()
time = endTime - startTime
print(time)

print("The Prime Factor pair for the number", str(userInput), "is:", primeFactors)
##print("\nPress any key to close")
##input()

digits = len(str(userInput))

if len(primeFactors) > 0:

    with open(r'rtcQuantum.csv', 'a', newline='') as csvfile:
        fieldnames = ['Number','Digits', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writerow({'Number': str(userInput), 'Digits': str(digits), 'Time': str(time)})

    


