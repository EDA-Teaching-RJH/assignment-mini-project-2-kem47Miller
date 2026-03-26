
#File Manager for the Arcade Card System that Handles reading from and writing to CSV files

from arcadians import Arcade_card

def load_accounts(filename):
   
    pirates = []  # Empty list to store cards
    
    try:
        # Open file for reading
        with open(filename, "r") as file:
            # Read each line one by one
            for line in file:
                line = line.strip()  # Remove newline and extra spaces
                
                # Skip empty lines
                if not line:
                    continue
                
                # Split CSV line by commas so it is easier to work with
                parts = line.split(",")
                
                # Check we have exactly 4 fields
                if len(parts) == 4:
                    privateer = parts[0]      # Player name
                    arcade_login = parts[1]   # Card ID
                    
                    # Convert balance to integer, helps prevent errors
                    try:
                        doubloons = int(parts[2])
                    except ValueError:
                        doubloons = 0   # Default to 0 if invalid
                    
                    status = parts[3] # Card status
                    
                    # Create card object
                    card = Arcade_card(privateer, arcade_login, doubloons)
                    
                    # Set the status (since constructor defaults to "Exists")
                    card.status = status
                    
                    pirates.append(card)
        
        print(f"Loaded {len(pirates)} accounts from {filename}")
        
    except FileNotFoundError:
        print(f"No existing file found: {filename}. Starting fresh.")
    except Exception:
        print("Error loading file")
    
    return pirates

def save_accounts(filename, pirates):
   
    try:
        # Open file for writing
        with open(filename, "w") as file:
            # Write each card as a CSV line
            for p in pirates:
                # Format: privateer,arcade_login,doubloons,status
                line = f"{p.privateer},{p.arcade_login},{p.doubloons},{p.status}\n"
                file.write(line)
        
        print(f"Saved {len(pirates)} accounts to {filename}")
        return True
        
    except Exception:
        print("Error saving file")
        return False
def export_to_txt(filename, pirates):
    
    try:
        with open(filename, "w") as file:
            file.write("ARCADE CARD REPORT\n")
            file.write("-------------------------\n")
            file.write("\n")#just for spacing
            
            for p in pirates:
                file.write(f"Player: {p.privateer}\n")
                file.write(f"Card ID: {p.arcade_login}\n")
                file.write(f"Balance: {p.doubloons} doubloons\n")
                file.write(f"Status: {p.status}\n")
                file.write("-----------------------------------\n")
                file.write("\n")#add extra line for spacing
        
        print(f"Report saved to {filename}")
        return True
        
    except Exception:
        print("Error saving report")
        return False