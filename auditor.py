
maxinventory=500
inventory=0 #type int
FailedReject=0
FinalExceed=0
while True:
    inventoryadd=input("Enter stock quantity:" )
    if inventoryadd == "quit":
        print("Total units processed is:", inventory, " Number of entries failed or rejected:", failedReject)
        break
    elif inventoryadd.isdigit()== False:
        print("Invalid input, please enter positive numbers")
        failedReject=failedReject + 1
    else:
        inventoryadd=int(inventoryadd)
        inventory=inventory + inventoryadd
        print("Current total inventory:", inventory)