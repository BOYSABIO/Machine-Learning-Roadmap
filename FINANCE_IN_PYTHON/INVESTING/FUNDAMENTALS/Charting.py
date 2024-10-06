import matplotlib.pyplot as plt
import pandas as pd

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

    for asset, percentage in balances.items():
        percentage = int(input("Enter amount for {}:".format(asset)))
        
        sum += percentage
        print(sum)
        
            
        balances.update({asset:percentage})
        print("Updated: \n", asset + ': ', percentage)
    
    return balances

create_allocation()
dict = {
    'Asset_type':['Cash', 'Fund', 'Stock'],
    'Amount':[1400, 500, 600]
}

df = create_allocation()

fig, ax = plt.subplots()
myexplode = [0.2, 0, 0]
df.value_counts().plot(kind = "pie", explode = myexplode)
ax.set_title('Portfolio Allocation', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel('')

plt.show()

save = input('Would you like to save?: ')
if save == 'yes':
    plt.savefig(input('File name: '))

