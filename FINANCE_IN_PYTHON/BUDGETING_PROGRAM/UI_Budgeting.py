import math
import pandas as pd
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

def test():
    print("Starting General Program...")
    print("---------------------------")
    income = int(input("Enter income: "))
    expense = int(input("Enter expense: "))
    net = income - expense

    # Add allowance
    allowance = 600
    check = input("Do you want to add allowance?: ")
    if check == "yes":
        total = net + allowance
    else:
        total = net
    
    # Initialize Basic Needs
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    ff_days = fast_food / 20

    # Initialize Finance Variables
    savings = total * 0.2
    remainder = round(((total - (grocery + fast_food + savings))), 2)

    stocks = round((remainder * 0.7), 2)
    bonds = round((remainder * 0.1), 2)
    Saving = (savings / 2)
    Roth_IRA = (savings / 2)
    schwab = Saving + Roth_IRA + stocks + bonds
    fun = round((remainder - (stocks + bonds)), 2)

    # Create & Print Dictionary
    dict = {
    "Income":total,
    "Grocery":grocery,
    "Fast_Food":fast_food,
    "Total Food":total_food,
    "Saving":Saving,
    "Roth_IRA":Roth_IRA,
    "Remainder":remainder,
    "Stocks":stocks,
    "Bonds":bonds,
    "Schwab Total":schwab,
    "Fun":fun
    }

    print(dict)
    s = pd.Series(dict)
    print(s)

    print()
    print("Extra Points:")
    print("Grocery amount per week: ", round((grocery / 4),2))
    print()
    print("Number of fast food deliveries under 20: ", round(ff_days))
    print("Every ", round(((ff_days / 31) * 7),3) , "days, you can order 20€ fast food")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Login System", font=("Aptos", 24))
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text = "Username")
entry1.pack(pady = 12, padx = 10)

"""entry2 = customtkinter.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12, padx = 10)"""

button1 = customtkinter.CTkButton(master = frame, text = "TEST", command = test)
button1.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "Login", command = login)
button.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember Me")
checkbox.pack(pady = 12, padx = 10)

root.mainloop()
