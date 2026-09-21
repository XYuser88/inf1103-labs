#logic to audit inventory and reject invalid entries
#inventory set 0 , failedreject set to 500
#while inventory below 500, 
# enter and add stock quantity to inventory

#if "quit", show full quantity and failed rejected
#else, continue with loop

inventory=0 #type int
failedReject=0
FinalExceed=0

def get_input():
        inventoryadd=input("Enter stock quantity:" )
        if inventoryadd == "quit":
            return "quit"
        elif inventoryadd.isdigit() == False:
            print("Invalid input, please enter an integers")
            return None # invalid input trigger
        elif int(inventoryadd) < 0:
            print("please input positive integers")
            return None # invalid input trigger
        else:
            return int(inventoryadd)

def process_delivery(current_total, new_amt):
    new_total = current_total + new_amt
    return new_total


def exceed_threshold(current_total):
    maxinventory=500
    if current_total > maxinventory: 
        return True

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total units processed is:", total_units, "\nNumber of entries failed or rejected:", failed_attempts, "\nTax amount:", calculate_tax(total_units))


#Input function -> processes delivery by adding them -> generate report that will also calculate the tax using the function in the generate report function


while True:
    new_value = get_input() 
    if new_value == "quit":
        break # break out of the while loop
    elif new_value == None:
        failedReject += 1

    else:
        inventory = process_delivery(inventory, new_value)
        tax = calculate_tax(new_value)
        print(f'Current Inventory: {inventory}')
        
    if exceed_threshold(inventory)==True:
        print("Inventory has exceeded maximum threshold of 500 units")
        break
    
generate_report(inventory, failedReject)
# end of program

#main program
# while True:
#     inventoryadd = get_input() -> the result
#     if inventoryadd == "quit": 
#         generate_report(inventory, failedReject) 
#         break
#     elif inventoryadd== None:
        
#         failedReject=failedReject + 1
#     else:
#         inventory=process_delivery(inventory, inventoryadd)
#         tax=calculate_tax(inventoryadd)
#         print("Current total inventory:", inventory)
#         print("Tax on this delivery is:", tax)

#     if inventory>maxinventory:
#         FinalExceed =inventory-maxinventory
#         print("Inventory has exceeded maximum threshold by:",FinalExceed, " units")
#         break
#     else:
#         continue



# def main():
#   global inventory, failedReject
#   while True:
#       result = get_input()
#       if result is None:
#           generate_report(inventory, failedReject)
#           break
#       else:
#           inventory = process_delivery(inventory, result)
#           print(f'Updated Inventory: {inventory}')
#           if inventory >= 500:
#               print('Inventory exceeds 500. Ending Program')
#               generate_report(inventory, failedReject)    
#               break

# main()
