
#File Manager for the Arcade Card System that Handles reading from and writing to CSV files

"""
File Manager for Arcade Card System
Handles reading from and writing to CSV files
"""

import csv
from arcadians import Arcade_card

def load_accounts(filename):

    #Read from CSV file - loads existing card data
    
    
    pirates = []
    
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                privateer = row["privateer"]
                arcade_login = row["arcade_login"]
                doubloons = int(row["doubloons"])
                status = row["status"]
                
                card = Arcade_card(privateer, arcade_login, doubloons)
                card.status = status
                pirates.append(card)
        
        print(f"Loaded {len(pirates)} accounts from {filename}")
        
    except FileNotFoundError:
        print(f"No existing file found: {filename}. Starting fresh.")
    except Exception:
        print("Error loading file")
    
    return pirates


def save_accounts(filename, pirates):
    
    #Write to CSV file - saves all card data.Having csv.DictWriter makes for cleaner code
    
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["privateer", "arcade_login", "doubloons", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()  # Writes the header row
            
            for p in pirates:
                writer.writerow({
                    "privateer": p.privateer,
                    "arcade_login": p.arcade_login,
                    "doubloons": p.doubloons,
                    "status": p.status
                })
        
        print(f"Saved {len(pirates)} accounts to {filename}")
        return True
        
    except Exception:
        print("Error saving file")
        return False


def export_to_txt(filename, pirates):
    
    #Write to TEXT file - creates readable report
    
    try:
        with open(filename, "w") as file:
            file.write("ARCADE CARD REPORT\n")
            file.write("-------------------------\n")
            file.write("\n")
            
            for p in pirates:
                file.write(f"Player: {p.privateer}\n")
                file.write(f"Card ID: {p.arcade_login}\n")
                file.write(f"Balance: {p.doubloons} doubloons\n")
                file.write(f"Status: {p.status}\n")
                file.write("-----------------------------------\n")
                file.write("\n")
        
        print(f"Report saved to {filename}")
        return True
        
    except Exception:
        print("Error saving report")
        return False

