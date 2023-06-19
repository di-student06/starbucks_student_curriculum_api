from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COFFEE = {
    "Latte": {
        "coffee_name": "Latte",
        "milk": "Whole",
        "timestamp": get_timestamp()
    },
    "Cappuccino": {
        "coffee_name": "Cappuccino",
        "milk": "Oat",
        "timestamp": get_timestamp()
    },
    "FlatWhite": {
        "coffee_name": "FlatWhite",
        "milk": "Soy",
        "timestamp": get_timestamp()
    }
}

# Create a handler for coffee get route
def read():
    """
    This function responds to a request for /api/coffee
    with the complete lists of coffee drinks
    """
    # Create the list of coffee from our data
    return [COFFEE[key] for key in sorted(COFFEE.keys())]

# STUDENT DO Create a get route that accepts a parameter to return one drink
# SOLUTION