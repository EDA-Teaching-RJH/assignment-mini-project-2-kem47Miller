import re

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


