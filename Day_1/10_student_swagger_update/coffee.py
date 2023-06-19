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
        "coffee_name": "Flat White",
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

def read_one(coffee_name):
    """
    This function responds to a request for /api/coffee/{coffee}
    with one matching coffee from coffee
    :param coffee:   name of coffee drink to find
    :return:        coffee matching the name
    """
    # Does the coffee exist in COFFEE?
    if coffee_name in COFFEE:
        coffee = COFFEE.get(coffee_name)

    # otherwise, nope, not found
    else:
        abort(
            404, "Coffee with name {coffee_name} not found".format(coffee_name=coffee_name)
        )

    return coffee    

def create(coffee):
    """
    This function creates a new drink in the coffee object
    :param coffee:  coffee drink to create
    :return:        201 on success, 406 if drink exists
    """
    coffee_name = coffee.get("coffee_name", None)
    milk = coffee.get("milk", None)

    # Does the drink already exist?
    if coffee_name not in COFFEE and coffee_name is not None:
        COFFEE[coffee_name] = {
            "coffee_name": coffee_name,
            "milk": milk,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{coffee_name} successfully created".format(coffee_name=coffee_name), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Coffe, {coffee_name}, already exists".format(coffee_name=coffee_name),
        )

# STUDENT DO: Update the put request to also update the milk value  