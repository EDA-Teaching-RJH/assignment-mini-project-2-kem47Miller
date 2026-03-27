# Import all the functions and classes from other files
from arcadians import Arcade_card
from custom import checking_arcade_login, validate_amount, get_amount_value, validate_name, calculate_stats
from custom import get_median, get_mode, get_stdev
from file_manager import load_accounts, save_accounts, export_to_txt

# Constants - fixed values used throughout the program
FILENAME = "pirate.csv"                      # CSV file for saving data
EXPORT_FILENAME = "arcade_report.txt"        # Text file for reports

# Load existing accounts when program starts
print("---------------------------")
print("ARCADE CARD SYSTEM")
print("-----------------------")
pirates = load_accounts(FILENAME)  # Read from CSV file
print(f"System ready. {len(pirates)} cards loaded.")

def create_card():
    #Create a new arcade card
    print("-------------------------~~\n")
    print("CREATE NEW CARD")
    print("--------------------------~~~~\n")
    
    # Get player name
    name = input("Enter player name: ").strip()
    if not name:
        print("Error: Player name cannot be empty")
        return
    
    # Name is validated using regex from custom.py
    if not validate_name(name):
        return
    
    # Get card ID
    card_id = input("Enter card ID (format: PIRT00001): ").strip().upper()
    
    # validate card id format using regex from custom.py
    if not checking_arcade_login(card_id):
        return
    
    # Check if card ID already exists already
    for p in pirates:
        if p.arcade_login == card_id:
            print(f"Error: Card ID {card_id} already exists!")
            return
    
    # Create new card 
    new_card = Arcade_card(name, card_id)
    pirates.append(new_card)
    print(f"Success! Card created for {name}")
    print(f"Total cards in system: {len(pirates)}")

def view_cards():
    #Display all cards
    print("************---------------\n")
    print("VIEW ALL CARDS")
    print("---------------************\n")
    
    if len(pirates) == 0:
        print("No cards available in system")
    else:
        print(f"Showing {len(pirates)} cards:")
        print()
        for p in pirates:
            p.view()  # Call the view method from Arcade_card class

def view_card_details():
    #View detailed statistics for a specific card
    print("----~~~~~~--------\n")
    print("CARD DETAILED STATISTICS")
    print("--------~~~~~~-")
          
    card_id = input("Enter card ID: ").strip().upper()
    
    for p in pirates:
        if p.arcade_login == card_id:
            p.view_detailed_stats()  # Show detailed stats for this card
            return
    
    print("Card not found")

def add_credits():
    #Add credits to a card
    print("-------------------\n")
    print("ADD CREDITS")
    print("---------------")
    
    card_id = input("Enter card ID: ").strip().upper()
    
    for p in pirates:
        if p.arcade_login == card_id:
            print(f"Current balance: {p.doubloons} doubloons")
            amount_str = input("Enter doubloons to add: ")
            
           # First check if valid
            if validate_amount(amount_str):
                amount = get_amount_value(amount_str)
                p.top_up(amount)
            return
    
    print("Card not found")

def play_game():
    #Playing a game will deduct credits from a card
    print("----------~~~~~~~-----\n")
    print("PLAY GAME")
    print("-----------")
    
    card_id = input("Enter card ID: ").strip().upper()
    
    for p in pirates:
        if p.arcade_login == card_id:
            print(f"Current balance: {p.doubloons} doubloons")
            try:
                price_input = input("Enter game price: ")
                price = int(price_input)
                if price <= 0:
                    print("An error has occurred. The price must be positive")
                    return
                p.pricing(price)
            except ValueError:
                print("An error has occurred. Please enter a valid number")
            return
    
    print("Card not found")
