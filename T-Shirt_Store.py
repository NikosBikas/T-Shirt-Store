# Import the modules needed to run the script.
import sys, time
from Lib.context import Call, User_Input, print_banner, clear

# Main definition - constants
menu_actions  = {}
tshirt_list = []

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    clear()
    print_banner()
    print ("Main Menu:")
    print ("")
    print ("1 Add a T-shirt to the Cart  ")
    print ("2 View Items in the Cart  ")
    print ("3 Check Out ")   
    print ("0 Quit")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            menu_actions['main_menu']()
    return

# Menu Item Add New Product!
def shirtToCart():
    clear()
    print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
    User_Input.tshirt_buy(tshirt_list)
    input("")
    return main_menu()

def viewCart():
    clear()
    print_banner("- Here you can view all the items that were added to the shopping Cart -")
    Call.ViewCart(tshirt_list)
    return main_menu()

def transaction():
    clear()
    print_banner("- Transaction using the Strategy models! -")
    Call.Transaction(tshirt_list)
    return main_menu()

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    print('buy')
    time.sleep(1)
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': shirtToCart,
    '2': viewCart,
    '3': transaction,
    '9': back,
    '0': exit,
}



# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
