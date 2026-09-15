

inventory=0 #type int
while True:
    inventoryadd=input("Enter stock quantity:" )
    if inventoryadd == "quit":
        print("Total units processed is:", inventory, " Number of entries failed or rejected:", failedReject)
        break
    elif 