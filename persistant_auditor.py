#try read file if file not found initialize inventory =0
#get_input function, get input then convert input to int
#calculate tax, and shows current tax, total value and failed entries
#save the output to file
failedRejectcount=0
FinalExceed=0
inventorylist=[]
def load_inventory():
    global inventory,inventorylist
    try:
        with open("inventory.txt","r") as file:
            transaction = file.readlines()
            inventory = int(transaction[0].split(": ")[1])

            for transaction in transaction[2:]:
                inventorylist.append(int(transaction))
            print(inventory)
            
    except FileNotFoundError: # only runs if error exists
        # insert new code to set inventory as 0 first
            inventory = 0
            print(inventory)


def get_input():
        global inventory, failedRejectcount
        inventoryadd=input("Enter stock quantity:" )
        if inventoryadd == "quit":
            return "quit"
        elif inventoryadd.isdigit() == False:
            print("Invalid input, please enter an integers")
            failedRejectcount += 1
            return None # invalid input trigger
        elif int(inventoryadd) < 0:
            print("please input positive integers")
            failedRejectcount += 1
            return None # invalid input trigger
        else:
            
            return int(inventoryadd)

def process_delivery(current_total, new_amt):
    current_total = current_total + new_amt
    return current_total


def exceed_threshold(current_total):
    maxinventory=500
    if current_total > maxinventory: 
        return True

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def Saveinventoryfile():
    global inventory
    with open("inventory.txt", 'w') as file:
        file.write('Inventory: ')
        file.write(str(inventory))
        file.write("\n")
        file.write("inventory list: \n")

        for transaction in inventorylist:
            file.write(str(transaction) +"\n")
    




def generate_report(total_units, failed_attempts):
    print("Total units processed is:", total_units, "\nNumber of entries failed or rejected:", failed_attempts, "\nTax amount:", calculate_tax(total_units))


#Input function -> processes delivery by adding them -> generate report that will also calculate the tax using the function in the generate report function



load_inventory()

while True:
    new_value = get_input() 
    if new_value == "quit":
        Saveinventoryfile()
        break # break out of the while loop
    elif new_value == None:
        continue

    else:
        inventory = process_delivery(inventory, new_value)
        inventorylist.append(new_value)
        tax = calculate_tax(new_value)
        print("current inventory:", inventory)

    if exceed_threshold(inventory)==True:
        print("Inventory has exceeded maximum threshold of 500 units")
        Saveinventoryfile()
        break
    
generate_report(inventory, failedRejectcount)




