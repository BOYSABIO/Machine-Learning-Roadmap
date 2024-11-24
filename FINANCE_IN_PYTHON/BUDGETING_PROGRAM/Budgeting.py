import math
from numpy import real
import pandas as pd
import calendar
import datetime
from tabulate import tabulate

def general(income, expense):
    net = income - expense
    allowance = 600
    check = input("Do you want to add allowance?: ")
    if check == "yes":
        total = net + allowance
    else:
        total = net

    grocery, fast_food, total_food, ff_days = basic_needs(total)
    days_in_month = datecheck()

    # initialize subscriptions
    subscriptions_total = 0

    investment_style = input("Choose (safe) or (risky) investment style: ") #Choose conservative or risky style for rebalancing
    dict = finance(total, grocery, fast_food, total_food, subscriptions_total, investment_style)
    
    s = pd.Series(dict)

    print('PORTIONING')
    print('---------------------------')
    print(s[0:4])
    print('---------------------------')
    print('SAVINGS / SUBS')
    print('---------------------------')
    print(s.iloc[4:8])
    print('---------------------------')
    print('INVESTING')
    print('---------------------------')
    print(s.iloc[8:15])
    print('---------------------------')
    print('FUN')
    print('---------------------------')
    print(s.iloc[15])
    print('---------------------------')

    print()
    print('---------------------------')
    print("Extra Statistics:")
    print('---------------------------')
    print("Grocery amount per week: ", round((grocery / 4),2))
    print("Grocery amount per day: ", round((grocery / days_in_month),3))
    print('---------------------------')
    print()
    print('---------------------------')
    print("Number of fast food deliveries under $20: ", round(ff_days))
    print("Every ", round((days_in_month / ff_days),3) , "days, you can order 20€ fast food")
    print('---------------------------')
    print()

def basic_needs(total):
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    ff_days = fast_food / 20
    return grocery, fast_food, total_food, ff_days

def datecheck():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    days_in_month = calendar.monthrange(year,month)[1]
    return days_in_month

def finance(total, grocery, fast_food, total_food, subscriptions_total, investment_style):
    savings = total * 0.2
    remainder = round(((total - (total_food + subscriptions_total + savings))), 2)
    fun = round((remainder * 0.2), 2)
    allocation = remainder - fun
        
    if investment_style == "safe":
        stocks = round((allocation * 0.25), 2)
        bonds = round((allocation * 0.40),2)
        realestate = round((allocation * 0.1),2)
        commodities = round((allocation * 0.1),2)
        money_fund = round((allocation * 0.15))
    else:
        stocks = round((allocation * 0.4), 2)
        bonds = round((allocation * 0.3), 2)
        realestate = round((allocation * 0.1),2)
        commodities = round((allocation * 0.15), 2)
        money_fund = round((allocation * 0.05),2)
        
    Saving = (savings / 3)
    Roth_IRA = (savings / 3)
    e_fund = (savings / 3)
    schwab = Roth_IRA + stocks + bonds + realestate + commodities + money_fund

    dict = {
        "Income":total,
        "Grocery":grocery,
        "Fast_Food":fast_food,
        "Total Food":total_food,
        "Subscriptions":subscriptions_total,
        "N26 Saving":Saving,
        "Roth_IRA":Roth_IRA,
        "Emergency Fund":e_fund,
        "Remainder":remainder,
        "Stocks":stocks,
        "Bonds":bonds,
        "REITs":realestate,
        "Commodities":commodities,
        "Money Market Fund":money_fund,
        "Schwab Total":schwab,
        "Fun":fun
        }
    
    return dict


while True:
    print("1 ---- General")
    print("2 ---- Money Check")
    print("3 ---- Rebalancing")
    print("4 ---- Exit")
    program = int(input("Please indicate: "))
    if program == 1:
        print("Starting General Program...")
        print("---------------------------")
        income = int(input("Enter income: "))
        expense = int(input("Enter expense: "))
        general(income, expense)

    elif program == 2:
        print("Starting Money Check...")
        print("---------------------------")
        check = input("Do you want to allocate savings / investments?: ")

        if check == "yes":
            # we include the savings and investments allocation
            # also include numbers regarding the amount that has been spent already
            # how well have you done such as expenses per day or amount remaining
            income_at_start_of_month = int(input("Enter starting amount: "))
            balance = int(input("Enter Balance: "))
            money_spent = income_at_start_of_month - balance
    
            # Initialize Basic Needs
            grocery = (balance * 0.075) * 4
            fast_food = (balance * 0.075) * 4
            total_food = grocery + fast_food
            ff_days = fast_food / 20

            # Calculate number of days remaining in month
            now = datetime.datetime.now()
            last_day = datetime.datetime(now.year, now.month + 1, 1) - datetime.timedelta(days = 1)
            remaining_days = (last_day - now).days + 1

            # Initialize Subscribtions
            subscriptions_total = "Paid"

            # Initialize Finance Variables
            savings = balance * 0.2
            remainder = round(((balance - (total_food + savings))), 2)

            stocks = round((remainder * 0.7), 2)
            bonds = round((remainder * 0.1), 2)
            Saving = (savings / 2)
            Roth_IRA = (savings / 2)
            schwab = Saving + Roth_IRA + stocks + bonds
            fun = round((remainder - (stocks + bonds)), 2)

            # Create & Print Dictionary
            dict = {
            "Current Balance":balance,
            "Money Spent":money_spent,
            "Grocery":grocery,
            "Fast_Food":fast_food,
            "Total Food":total_food,
            "Subscriptions":subscriptions_total,
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
            print("Every ", round((remaining_days / ff_days),3) , "days, you can order 20€ fast food")
        else:
            # Most importantly we need to have the program to use the starting amount from the month to extract the
            #amount of money that has already been allocated to investments and savings so that the final result of
            #spending amount isn't skewed because there is money spent from the start in savings & investments
            # we only include the amount that goes towards groceries for the rest of the month
            # also include numbers regarding the amount that has been spent already
            # how well have you done such as expenses per day or amount remaining
            income_at_start_of_month = int(input("Enter starting amount: "))
            balance = int(input("Enter Balance: "))
            money_spent = income_at_start_of_month - balance

    elif program == 3:
        print("Rebalancing Program...")
        amount = int(input("Enter the amount to be rebalanced: "))
        investment_style = input("Choose (safe) or (risky) investment style: ")

        if investment_style == "safe":
            stocks = round((amount * 0.25), 2)
            bonds = round((amount * 0.40),2)
            realestate = round((amount * 0.1),2)
            commodities = round((amount * 0.1),2)
            money_fund = round((amount * 0.15))
        else:
            stocks = round((amount * 0.4), 2)
            bonds = round((amount * 0.3), 2)
            realestate = round((amount * 0.1),2)
            commodities = round((amount * 0.15), 2)
            money_fund = round((amount * 0.05),2)

        rebalance = {
            "Stocks":stocks,
            "Bonds":bonds,
            "REITs":realestate,
            "Commodities":commodities,
            "Money Market":money_fund
        }

        print(rebalance)
        s = pd.Series(rebalance)
        print(s)

    elif program == 4:
        print("Ending Program...")
        break
     









def food(total):
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    return grocery, fast_food, total_food

#grocery, fast_food, total_food = food(total)

def finance(total):
    savings = total * 0.2
    remainder = round(((total - (grocery + fast_food + savings))), 2)

    stocks = round((remainder * 0.7), 2)
    bonds = round((remainder * 0.1), 2)
    Saving = (savings / 2)
    Roth_IRA = (savings / 2)
    schwab = Saving + Roth_IRA + stocks + bonds
    fun = round((remainder - (stocks + bonds)), 2)
    return remainder, stocks, bonds, Saving, Roth_IRA, schwab, fun

#remainder, stocks, bonds, Saving, Roth_IRA, schwab, fun = finance(total)

# When you are in middle of the month (calculate how much left for grocery / fast food)
def money_check(grocery, fast_food):
    balance = int(input("Enter balance: "))
    print(balance)
    difference = (grocery + fast_food) - balance
    remainder_for_food = balance - grocery
    amount_per_week = round((grocery / 4),2)
    balance_per_week = round((balance / 4), 2)
    remainder_per_week = balance_per_week - amount_per_week

    return print(difference, remainder_for_food, amount_per_week, balance_per_week, remainder_per_week)



# Create a per week converter
def per_week(value):
    now = datetime.datetime.now()
    month_days = calendar.monthrange(now.year, now.month)[1]
    per_week = value / month_days
    return per_week


# Quick add for expenses (food / grocery / other)
# def quick_add():

#money_check(grocery, fast_food)



