import re

def is_valid_phone_number(input_value):
    
    # this regular expressions only matches valid phone numbers
    regex = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
    
    try: 
        # match input value against the regular expression
        # fullmatch tries to match the complete input value against the re
        # if a match is made, it returns a match Object
        # if no match is made it returns None
        match = re.fullmatch(regex, input_value)
    except:
        # if the match fails for whatever reason, return False
        return False

    # if a match is made, return True
    if match is not None:
        return True

    # in all other cases return false
    return False
