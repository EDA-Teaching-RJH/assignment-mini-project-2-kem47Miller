import re
import statistics

def checking_arcade_login(arcade_login):
    #pattern should be PIRT then 5 numbers for Id format
    pattern = r"^PIRT\d{5}$"
    
    # Check if string matches pattern
    if re.match(pattern, arcade_login):
        return True
    else:
        print("Invalid format. Use PIRT followed by 5 digits (e.g., PIRT00001)")
        return False


def validate_name(name):
   # Pattern: letters, spaces, hyphens only (one or more)
    pattern = r"^[A-Za-z\s\-]+$"
    
    if re.match(pattern, name):
        return True
    else:
        print("Please ensure your name contains only letters, spaces, and hyphens")
        return False


def validate_amount(amount):
    
    try:
        # Try to convert to integer
        amount_value = int(amount)
        
        # Check if positive
        if amount_value > 0:
            return True, amount_value
        else:
            print("Amount must be positive")
            return False, 0
    except ValueError:
        print("Please enter a valid number")
        return False, 0
def calculate_stats(doubloons_list):
   
    # Handle empty list
    if not doubloons_list:
        return {
            "total": 0,
            "average": 0,
            "max": 0,
            "min": 0,
            "count": 0
        }
    
    # Calculate stats
    total = sum(doubloons_list)
    count = len(doubloons_list)
    average = total / count
    maximum = max(doubloons_list)
    minimum = min(doubloons_list)
    
    # Return as dictionary
    return {
        "total": total,
        "average": average,
        "max": maximum,
        "min": minimum,
        "count": count
    }  