#logic to audit inventory and reject invalid entries
#inventory set 0 , failedreject set to 500
#while inventory below 500, 
# enter and add stock quantity to inventory

#if "quit", show full quantity and failed rejected
#else, continue with loop

maxinventory=500
inventory=0 #type int
failedReject=0
FinalExceed=0
#while True:
    #inventoryadd=input("Enter stock quantity:" )
    #if inventoryadd == "quit":
        #print("Total units processed is:", inventory, " Number of entries failed or rejected:", failedReject)
        #break
    #elif inventoryadd.isdigit()== False:
        #print("Invalid input, please enter positive numbers")
        #failedReject=failedReject + 1
    #else:
        #inventoryadd=int(inventoryadd)
        #inventory=inventory + inventoryadd
        #print("Current total inventory:", inventory)

    #if inventory>maxinventory:
        #FinalExceed =inventory-maxinventory
        #print("Inventory has exceeded maximum threshold by:",FinalExceed, " units")
        #break
    #else:
        #continue

def get_input():
        inventoryadd=input("Enter stock quantity:" )
        if inventoryadd == "quit":
            return "quit"
        elif inventoryadd.isdigit()==False:
            return None
        return int(inventoryadd)

def process_delivery(current_total, new_amt):
    new_total = current_total + new_amt
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total units processed is:", total_units)
    print("Number of entries failed or rejected:", failed_attempts)