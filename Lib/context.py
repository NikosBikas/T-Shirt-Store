
from Lib.strategy import PayByCredit,PayByBank,PayByCash
import os,platform

# Function that Checks User OS For Clearing The Screen
def clear():
	if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
		os.system('cls') 
	else:
		os.system('clear')

# Banner! 
def print_banner(title="Welcome to my Store - Software ver:0.01 - Author: Nikolaos Bikas"):
    print("""
███████╗██╗  ██╗██╗██████╗ ████████╗    ███████╗████████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║  ██║██║██╔══██╗╚══██╔══╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
███████╗███████║██║██████╔╝   ██║       ███████╗   ██║   ██║   ██║██████╔╝█████╗  
╚════██║██╔══██║██║██╔══██╗   ██║       ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
███████║██║  ██║██║██║  ██║   ██║       ███████║   ██║   ╚██████╔╝██║  ██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
""")
    total_len = 85
    if title:
        padding = total_len - len(title) - 4
        print("= {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 

class Shirt_Characteristics: #This is the context class for the strategy Pattern
    color = ['red','orange','yellow','green','blue','indigo','violet'] #In this line and above  are the lists with the accepted inputs for color,size,fabric and payment
    size = ['xs','s','m','l','xl','xxl','xxxl']
    fabric = ['wool','cotton','polyester','rayon','linen','cashmere','silk']
    payment = ['credit','bank','cash']

    #dictionaries with the price of each color,size and fabric
    color_prices={'red': 7 , 'orange': 5.70 , 'yellow': 5.60, 'green': 5.90 , 'blue': 6.20 , 'indigo': 7.30,'violet': 6.60 }
    size_prices={'xs': 5, 's': 5.5, 'm': 6.5, 'l': 7.2, 'xl': 7.8, 'xxl': 8, 'xxxl':8.5}
    fabric_prices={'wool' : 10, 'cotton': 13, 'polyester': 11.5, 'rayon':14, 'linen': 12, 'cashmere':16, 'silk':15.5}
    
    def __init__(self, t_color, t_size, t_fabric, t_payment, strategy ) : #init of Shirt_Characteristics
        
        self._t_color = t_color
        self._t_size = t_size
        self._t_fabric = t_fabric
        self._t_payment = t_payment
        self._strategy = strategy

    #Properties and setters for getting the protected attributes
    @property
    def t_color(self):
        return self._t_color

    @property
    def t_size(self):
        return self._t_size

    @property
    def t_fabric(self):
        return self._t_fabric

    @property
    def t_payment(self):
        return self._t_payment

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter #setter for strategy so it can be redefined outside the class
    def strategy(self,value):
        self._strategy = value

        
    def executeStrategy(self): #The function that executes the chosen strategy
        return self._strategy.dopayment(self)

    def totalCost(self): # Function that culculates the total cost of each t-shirt object
        total_cost = self.color_prices[self.t_color] + self.size_prices[self.t_size] + self.fabric_prices[self.t_fabric]
        return total_cost

class User_Input:
    @staticmethod
    def checkChoices(message,options,errorMessage): ##function for checking the inputs (use for many cases. message for the user, options for values to check and errorMessage if something goes wrong
        inputVal = input(message).upper()
        while inputVal not in options:
            print(errorMessage)
            print()
            inputVal = input(message).upper()
        return inputVal
    
    @staticmethod
    def tshirt_buy(tshirt_list,case=False): #function for t-shirt transaction
        if case:
            print('Please give the info for the t-shirt you want to buy.\n')
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe Colors: "+','.join([color.capitalize() for color in Shirt_Characteristics.color])+".")
        Tshirt_color = User_Input.checkChoices("Give T-shirt's color: ",[color.upper() for color in Shirt_Characteristics.color],'Wrong color.Please give one of: '+','.join([color.capitalize() for color in Shirt_Characteristics.color])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe sizes: "+','.join([size.capitalize() for size in Shirt_Characteristics.size])+".")
        Tshirt_size = User_Input.checkChoices("Give T-shirt's size: ",[size.upper() for size in Shirt_Characteristics.size],'Wrong size.Please give one of: '+','.join([size.capitalize() for size in Shirt_Characteristics.size])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe fabric: "+','.join([fabric.capitalize() for fabric in Shirt_Characteristics.fabric])+".")
        Tshirt_fabric = User_Input.checkChoices("Give T-shirt's fabric: ",[fabric.upper() for fabric in Shirt_Characteristics.fabric],'Wrong fabric.Please give one of: '+','.join([fabric.capitalize() for fabric in Shirt_Characteristics.fabric])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("Please choose a payment method from the following list: "+','.join([payment.capitalize() for payment in Shirt_Characteristics.payment])+".")
        Tshirt_payment = User_Input.checkChoices("Give payment method: ",[payment.upper() for payment in Shirt_Characteristics.payment],'Wrong payment method.Please give one of: '+','.join([payment.capitalize() for payment in Shirt_Characteristics.payment])+'.').lower()

        new_Tshirt = Shirt_Characteristics ( t_color = Tshirt_color, t_size = Tshirt_size, t_fabric = Tshirt_fabric , t_payment = Tshirt_payment, strategy=None )
        tshirt_list.append(new_Tshirt) #fill the tshirt list with as many as tshirt user likes
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -") 
        anotherDec = User_Input.checkChoices("Want to add another t-shirt to the Cart? Type 'y' for yes and 'n' for no.",['Y','N'],'Wrong choice!') #ask user for adding another t-shirt
        if anotherDec == 'Y': #if yes fill inputs for another t-shirt
            User_Input.tshirt_buy(tshirt_list,case=True) 
        else:
            clear()
            print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
            print("T-shirt('s) added succesfully to the Cart.")
            print("\nPress Enter to return at the main menu...")
        return tshirt_list #return tshirt list to main module.

class Call(User_Input):

    @staticmethod
    def ViewCart(tshirt_list):
        if len(tshirt_list) == 0:
            print ("Shopping Cart is empty!")
            input('\nPress Enter to return at the main menu...')
            return
        else:      
            list_len= len(tshirt_list)
            print(f"Total items in the Cart:{list_len} \nWith the following characteristics:\n ")  
            for tshirt in tshirt_list: #for loop for printing all the t-shirts and check what strategy plan to apply depending on user's payment method choice.
                if tshirt.t_payment == 'credit' :
                    tshirt.strategy = PayByCredit() #apply the right strategy plan
                    print(tshirt.executeStrategy()) # call the right strategy plan
                    print('')
                elif tshirt.t_payment == 'bank' :               
                    tshirt.strategy = PayByBank()
                    print(tshirt.executeStrategy())
                    print('')
                else:
                    tshirt.strategy = PayByCash()
                    print(tshirt.executeStrategy())
                    print('')    
            input('\nPress Enter to return at the main menu...')
    
    @staticmethod
    def Transaction(tshirt_list):
        if len(tshirt_list) == 0:
            print ("Shopping Cart is empty!")
            input('\nPress Enter to return at the main menu...')
            return  
        else:      
            list_len= len(tshirt_list)
            print(f"Total items in the Cart:{list_len} \nWith the following characteristics:\n ")  
            for tshirt in tshirt_list: #for loop for printing all the t-shirts and check what strategy plan to apply depending on user's payment method choice.
                if tshirt.t_payment == 'credit' :
                    tshirt.strategy = PayByCredit() #apply the right strategy plan
                    print(tshirt.executeStrategy()) # call the right strategy plan
                    print('')
                elif tshirt.t_payment == 'bank' :               
                    tshirt.strategy = PayByBank()
                    print(tshirt.executeStrategy())
                    print('')
                else:
                    tshirt.strategy = PayByCash()
                    print(tshirt.executeStrategy())
                    print('')
            tshirt_list.clear()
            print('\nT-shirt transaction completed succesfully.')
            input('\nPress Enter to return at the main menu...')
                    
