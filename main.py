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