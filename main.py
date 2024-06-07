MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True



def process_selection(selection):
    global resources
    global is_on 
    if selection == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit:.2f}")
        run_machine()
    elif selection =='off':
        print('Good-bye.')
        is_on = False
        
    elif selection in ['espresso', 'latte', 'cappuccino']:
        enough = check_resources(selection)
        if enough == True:
            update_resources(selection)
            process_coins(MENU[selection]['cost'])
            profit_addition(selection)
            print(f'Here is your {selection}. Enjoy!')
            run_machine()
        else:
            run_machine()
    else:
        print('Invalid selection. Please try again.')
        run_machine()


def check_resources(selection):
    """Returns true if there are sufficient resources, false if not."""
    global resources
    for item in ['water', 'milk', 'coffee']:
        if resources[item] < MENU[selection]['ingredients'][item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True
    

def update_resources(selection):
    '''Subtracts the used ingredients from the resources.'''
    global resources
    for item in ['water', 'milk', 'coffee']:
        resources[item] -= MENU[selection]['ingredients'][item]
    return resources


def process_coins(cost):
    print(f'You owe ${cost:.2f}.  Please enter coins.')
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .1
    nickels = int(input("How many nickesl? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    total = quarters + dimes + nickels + pennies
    if total > cost:
        change = total - cost
        print(f'Your change is ${change:.2f}')
    elif total == cost:
        print(f'Thank you.')
    else:
        print('That is not enough money. Money refunded.')
        process_coins(cost)


def profit_addition(selection):
    '''Adds item amount to total profit.'''
    global profit
    profit += MENU[selection]['cost']
    return profit

def run_machine():
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    while is_on:
        process_selection(selection)
       

run_machine()