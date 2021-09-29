#Description: Simple elif program to determine cost of data breach based on industry and records
#Author: Jacob Bolar
#Date: 29-SEP-2021

print("""To determine the cost of a data breach in your organization, 
please provide your industry and the number of records breached.
(A breach record is one that contains personally identifiable
information such as SSN, credit card, CVV, etc.
when asked for 'Industry', please indicate one of the following:
	Communications\n\tRetail\n\tPharmaceutical\n\tEducation""")

#Dictionary of Cost amount per industry
Dict = {1: 316, 2: 286, 3: 259, 4: 237, 5: 236, 6: 223, 7: 219, 8: 209, 9: 204, 
        10: 196, 11: 183, 12: 181, 13: 172, 14: 125, 15: 93, 16: 73}
        
industry = ""
count = 0
totalCostAll = 0


#Method so we can keep elifs clean.  Calculates total cost of breach
def calcs(Dict):
	recordsBreached = int(input("Enter the Number of Records Breached: "))
	totalCost = int(recordsBreached * Dict)
	global totalCostAll 
	totalCostAll += int(totalCost)
	print("Cost of a ",recordsBreached," records data breach in " + industry + " is ",totalCost)
	global count
	count += 1


while industry != "quit":
	
	industry = input("\nPlease indicate the industry or type 'quit' to exit: ")

	if industry == "Communications":
		calcs(Dict[7])
			
	elif industry == "Retail":
		calcs(Dict[14])

	elif industry == "Pharmaceutical":
		calcs(Dict[8])

	elif industry == "Education":
		calcs(Dict[3])
	
	elif industry == "quit":
		print("Calculations Complete!")

	else:
		print("Unknown Industry")

averageCost = int(totalCostAll/count)
print("Number of Records Breached: ", count )
print("Total Cost of Records Breached: ", totalCostAll)
print("Average cost Per Breach: ", averageCost)
