#

try:
    with open("inventory.txt","r") as file:
        inventory = file.read()
        print(inventory)
except FileNotFoundError: # only runs if error exists
    # insert new code to make new file
    with open("inventory.txt", "w") as file:
        inventory = 0
        print(inventory)



