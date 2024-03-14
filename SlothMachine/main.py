import random

MAX_LINES = 3       #Convention in Python to show the fixed values
MAX_BET = 100
MIN_BET = 10
#Number of rows and columns the sloth Machine has
ROWS = 3
COLS = 3

#This is basically the symbol frequency
#Making a Symbol count dictionary
symbol_count = {
    "A":"2",    #Sloth machine has some valuable tokens, here A is the most valuable one of them
    "B":"4",
    "C":"6",
    "D":"8"
}
symbol_value = {
    "A": 5,    #These are values of how much each line of the symbol is actually worth
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                               #In the text line symbol is gonna be A and the symbol_count is the value assigned to it
    for symbol, symbol_count in symbols.items(): #using symbols.items because it gives both the key and the value associated with it
        for _ in range(int(symbol_count)):    #Added an int before the symbol count to resolve the error it gave
            all_symbols.append(symbol)


    columns = []     
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]   #slice operator is used ":" because current will store all values of all symbols and we make changes then it's visible too
        for _ in range(rows):
            value = random.choice(current_symbols)   #picks a random value from the list
            current_symbols.remove(value)            #it will remove the value so we don't pick same value again
            column.append(value)


        columns.append(column)

        
    return columns


def print_slot_machine(columns):   #Here we will transpose the given matrix from horizontal form to vertical form
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #here we use the if condition because we don't want a pipe symbol at the end of the list
            if i != len(columns) - 1:
                print(column[row], end = " | " )
            else:
                print(column[row], end = "")
        print()





def deposit(): #This function will collect user input to get the deposit from the user
    
    while True:
        amount = input("Enter the amount you'd like to deposit. $")
        if amount.isdigit():  #Checks if the entered value is a integer
            amount = int(amount)
            if amount > 0 and amount <= 10:  #Custom Change
                print("The minimum Amount should be greater than 10!")
            if amount > 10:
                break
            if amount<0:
                print("Invalid Amount!")

        else:
            print("Please Enter the Amount in Numbers!")

    return amount  

def get_no_of_lines():
    while True:
        lines = input(f"Enter the Number of lines to bet on from each line 1 - {MAX_LINES}  \n")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Please Enter a Valid Number of Lines!")
        else:
            print("Enter a Number!")

    return lines

def get_bet():
    while True:
        amount = input("Enter the Amount you would like to bet!")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The entered value must be in between ${MIN_BET} - ${MAX_BET}\n")
    
        else:
            print("The amount to bet should be in Numbers! ")

    return amount

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough balance !, Your current balance is {balance}")
            # get_bet()   #Custom Change used to reschedule the bet

        elif total_bet <= balance:
            break
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to {total_bet}")
    print("\n")
   

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won $ {winnings}. ")
    print(f"You won on the lines ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()  #Will store the entered value into the variable "balance"
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press Enter to play or press Q to quit!")
        if answer == "q" or spin == "Q":
            break
        balance += spin(balance)

    print(f"You left with ${balance} balance.")


    
main()