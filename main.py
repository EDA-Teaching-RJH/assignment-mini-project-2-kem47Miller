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
    
    print("Can not find card")

def block_card():
    #Block a card
    print("----------------\n")
    print("BLOCK CARD")
    print("------~~~~~~")
    
    card_id = input("Enter card ID to block: ").strip().upper()
    
    for p in pirates:
        if p.arcade_login == card_id:
            if p.status == "Blocked":
                print("Card is already blocked")
            else:
                p.block()
            return
    
    print("Oops, card not found")


def unblock_card():
    #Unblock a card
    print("--------------------\n")
    print("UNBLOCK CARD")
    print("~~~~~~~~~~~~~~~~~~~~")
    
    card_id = input("Enter card ID to unblock: ").strip().upper()
    
    for p in pirates:
        if p.arcade_login == card_id:
            if p.status == "Exists":
                print("Card is already active")
            else:
                p.unblock()
            return
    
    print("Sorry, but card not found")

def show_system_statistics():
    #Display comprehensive system statistics
    print("--------------\n")
    print("SYSTEM STATISTICS")
    print("~~~~~~~~")
    
    if len(pirates) == 0:
        print("No cards in system")
        return
    
    # Use the first card to access class-level statistics
    sample_card = pirates[0]
    
    # Get system-wide stats
    print("\n--- OVERALL SYSTEM STATISTICS ---")
    print(f"Total Cards Created (All Time): {sample_card.total_cards_all_time}")
    print(f"Total Doubloons Added (All Time): {sample_card.total_doubloons_all_time}")
    print(f"Total Games Played (All Time): {sample_card.total_games_all_time}")
    print(f"Total Doubloons Spent (All Time): {sample_card.total_spent_all_time}")
    
    # Current card status
    active_cards = [p for p in pirates if p.status == "Exists"]
    blocked_cards = [p for p in pirates if p.status != "Exists"]
    
    print("\n--- CURRENT CARD STATUS ---")
    print(f"Active Cards: {len(active_cards)}")
    print(f"Blocked Cards: {len(blocked_cards)}")
    
    # Balance statistics
    balances = [p.doubloons for p in pirates]
    balance_stats = calculate_stats(balances)
    
    print("\n--- CURRENT BALANCE STATISTICS ---")
    print(f"Total Balance in System: {balance_stats['total']} doubloons")
    print(f"Average Balance per Card: {balance_stats['average']:.2f} doubloons")
    print(f"Highest Balance: {balance_stats['max']} doubloons")
    print(f"Lowest Balance: {balance_stats['min']} doubloons")
    
    # Additional statistics using custom library
    print(f"Median Balance: {get_median(balances):.2f} doubloons")
    print(f"Mode Balance: {get_mode(balances)}")
    if len(balances) >= 2:
        print(f"Standard Deviation: {get_stdev(balances):.2f}")
    
    # Game statistics for current cards
    total_games = sum([p.total_individual_games for p in pirates])
    total_spent = sum([p.total_individual_spent for p in pirates])
    
    print("\n--- GAME STATISTICS ---")
    print(f"Total Games Played: {total_games}")
    print(f"Total Doubloons Spent: {total_spent}")
    
    if total_games > 0:
        avg_spent = total_spent / total_games
        print(f"Average Spent per Game: {avg_spent:.2f} doubloons")
    
    # Find richest player
    if balances:
        highest_balance = max(balances)
        for p in pirates:
            if p.doubloons == highest_balance:
                print(f"\n--- RICHEST PLAYER ---")
                print(f"Player: {p.privateer}")
                print(f"Balance: {p.doubloons} doubloons")
                break
    
    # Find most active player
    if total_games > 0:
        most_games = max([p.total_individual_games for p in pirates])
        for p in pirates:
            if p.total_individual_games == most_games and most_games > 0:
                print(f"\n--- MOST ACTIVE PLAYER ---")
                print(f"Player: {p.privateer}")
                print(f"Games Played: {p.total_individual_games}")
                print(f"Total Spent: {p.total_individual_spent} doubloons")
                break
    
    print("-----------------\n")

def export_report():
    #Export report to text file
    print("-------------------\n" )
    print("EXPORT REPORT")
    print("---------~~~~~~---")
    
    if len(pirates) == 0:
        print("It seems there are no cards to export")
        return
    
    if export_to_txt(EXPORT_FILENAME, pirates):
        print(f"Report saved as: {EXPORT_FILENAME}")

def save_and_exit():
    #Save all cards and exit program
    print("-------------------\n")
    print("SAVING AND EXITING")
    print("-----------------")
    
    save_accounts(FILENAME, pirates)
    print("~~~~~~~~~~~~~~")
    print("Goodbye!")
    print("~~~~~~~~~~~")
    return True

def show_menu():
    #Display the main menu
    print("-------------~~~~~~~~\n")
    print("MAIN MENU")
    print("----------------------")
    print("1. Create New Card")
    print("2. View All Cards")
    print("3. View Card Detailed Stats")
    print("4. Add Credits to Card")
    print("5. Play Game")
    print("6. Block Card")
    print("7. Unblock Card")
    print("8. Show System Statistics")
    print("9. Export Report to Text File")
    print("10. Save and Exit")
    print("-------------------------------")