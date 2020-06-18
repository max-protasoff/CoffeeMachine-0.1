water = 400
milk = 540
beans = 120
cups = 9
cash = 550

def change_qt(w = 0, m = 0, b = 0, cp = 0, csh = 0):
    global water, milk, beans, cups, cash
    
    water += w
    milk += m
    beans += b
    cups += cp
    cash += csh
    
def print_stat():
    global cash
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    if cash != 0:
     print(f'${cash} of money')
    elif cash == 0:
        print('0 of money')

def buy_coffee():
    type_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    if type_of_coffee == 'back':
         pass
    elif type_of_coffee == '1':
        if supply_check(w = -250, m = 0, b = -16, cp = -1) == False:
            change_qt(w = -250, m = 0, b = -16, cp = -1, csh = 4)
    elif type_of_coffee == '2':
        if supply_check(w = -350, m = -75, b = -20, cp = -1) == False:
            change_qt(w = -350, m = -75, b = -20, cp = -1, csh = 7)
    elif type_of_coffee == '3':
        if supply_check(w = -200, m = -100, b = -12, cp = -1) == False:
            change_qt(w = -200, m = -100, b = -12, cp = -1, csh = 6)
        
def supply_check(w = 0, m = 0, b = 0, cp = 0):
    if water >= -w and milk >= -m and beans >= -b and cups >= cp:
        print('I have enough resources, making you a coffee!')
        lack = False
        return lack
    elif water < -w:
        print('Sorry, not enough water!')
        lack = True
        return lack
    elif milk < -m:
        print('Sorry, not enough milk!')
        lack = True
        return lack
    elif beans < -b:
        print('Sorry, not enough coffee beans!')
        lack = True
        return lack
    elif cups < cp:
        print('Sorry, not enough disposable cups!')
         
        
def fill_machine():
    change_qt(w = int(input('Write how many ml of water do you want to add:')))
    change_qt(m = int(input('Write how many ml of milk do you want to add:')))
    change_qt(b = int(input('Write how many grams of coffee beans do you want to add:')))
    change_qt(cp = int(input('Write how many disposable cups of coffee do you want to add:')))
    
def take_money():
    print(f'I gave you ${cash}')
    change_qt(csh = -cash)

while True:
    command = input('Write action (buy, fill, take, remaining, exit):')
    if command == 'exit':
        break
    elif command == 'remaining':
        print_stat()
    elif command == 'buy':
        buy_coffee()
    elif command == 'fill':
        fill_machine()
    elif command == 'take':
        take_money()

    
