import json



# Open and change balances

# Open previous balances to allocate
def reallocation():
    with open(input("Enter allocation file name: ") + ".json", 'r') as file:
        balances = json.load(file)
    
    print(balances)

    for key, value in balances.items():
        print(key,value)
    
    item_to_change = input("What would you like to change?: ").capitalize()
    for key, value in balances.items():
        if key == item_to_change:
            balances.update({key:value, input("Enter new asset: ").capitalize():int(input("Enter new value: "))})
    
    #Make sure that the assets balance and in the event that they don't (display dictionary and ask to change)
    

# Create initial dictionary (Change to be dictionary inside  list)
def create_allocation():
    balances = {}
    balances_list = []
    sum = 0

    while True:
        new_item = input("Enter asset: ")
        if new_item == "":
            break
        balances.update({new_item.capitalize():0})
        balances_list.append(new_item.capitalize())
            
            

    print(balances)
    
    print()
    print("Initial Allocaton: ")

    while sum != 100:
        for asset, percentage in balances.items():
            percentage = int(input("Enter amount for {}:".format(asset)))
        
            sum += percentage
            print(sum)
        
            if (100 - percentage >= 0) & (sum <= 100):
                balances.update({asset:percentage})
                print("Updated: \n", asset + ': ', percentage, "\nSum = ", str(sum) + "%")
            else:
                print("Percentages do not align")
                sum = 0
                break
        
        
        
        
    

    print()
    print('Allocated')
    for asset, percentage in balances.items():
        print(asset + ': ', str(percentage) + '%')

    with open(input("Enter file name: ") + '.json', 'w') as file:
        json.dump(balances, file)

    print("File Saved")

create_allocation()
reallocation()