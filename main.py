# Import all the functions and classes from other files
from arcadians import Arcade_card
from custom import checking_arcade_login, validate_amount, validate_name, calculate_stats
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