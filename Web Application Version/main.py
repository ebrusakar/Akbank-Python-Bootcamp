


###############################################   Pizza Ordering System   #############################################


# Import the flask module to work on flask web application
from flask import Flask, render_template, request

# Import the datetime module to work with dates and times
from datetime import datetime




# Define a base Pizza class with a price and description attribute, and methods for getting the price and description
class Pizza:
    price = 0
    description = ""

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


# Define several subclasses of Pizza with different prices and descriptions
class Classic(Pizza):
    price = 9.99
    description = "Classic Pizza"


class Margherita(Pizza):
    price = 8.99
    description = "Margherita Pizza"


class TurkPizza(Pizza):
    price = 12.99
    description = "Turk Pizza"


class PlainPizza(Pizza):
    price = 10.99
    description = "Plain Pizza"


# Define a Decorator class that takes a Pizza component and adds additional functionality to it
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return Pizza.get_description(self) + ' ' + self.component.get_description()


# Define several subclasses of Decorator for adding toppings/sauces to pizzas, each with its own price and description
class Olives(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 1.5
        self.description = "Olives"


class Mushrooms(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 1.75
        self.description = "Mushrooms"


class GoatCheese(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 2.0
        self.description = "Goat Cheese"


class Meat(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 5.0
        self.description = "Meat"


class Onions(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 4.5
        self.description = "Onions"


class Corn(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 3.75
        self.description = "Corn"



def create_pizza(pizza_choice, sauce_choices):
    """
    Creates a pizza object with a chosen pizza base and sauce topping.

    Parameters:
    pizza_choice (str): A string representing the user's pizza choice.
    sauce_choices (list): A list of strings representing the user's sauce topping choices.

    Variables:
    base_pizza: A pizza object before any sauce toppings have been added
    
    Returns:
    topped_pizza: A pizza object with the chosen sauce topping added.

    """

    # Check the user's pizza choice and create a pizza object accordingly
    if pizza_choice == "Classic":
        pizza = Classic()
    elif pizza_choice == "Margherita":
        pizza = Margherita()
    elif pizza_choice == "TurkPizza":
        pizza = TurkPizza()
    elif pizza_choice == "PlainPizza":
        pizza = PlainPizza()


    # Check the user's sauce topping choices and add each sauce topping to the pizza object
    for sauce_choice in sauce_choices:
        if sauce_choice == "Olives":
            pizza = Olives(pizza)
        elif sauce_choice == "Mushrooms":
            pizza = Mushrooms(pizza)
        elif sauce_choice == "GoatCheese":
            pizza = GoatCheese(pizza)
        elif sauce_choice == "Meat":
            pizza = Meat(pizza)
        elif sauce_choice == "Onions":
            pizza = Onions(pizza)
        elif sauce_choice == "Corn":
            pizza = Corn(pizza)

    return pizza 


def calculate_price(pizza_size, pizza_type, toppings, quantity):
    # Price of pizza based on size
    if pizza_size == "Small":
        base_price = 1
    elif pizza_size == "Medium":
        base_price = 1.5
    else:
        base_price = 2

    topped_pizza = create_pizza(pizza_type, toppings)
    topped_pizza_cost = topped_pizza.get_cost()

    # Total price
    price = base_price * topped_pizza_cost * quantity
    return round(price, 2)

    


###############################################   Flask Web Application   #############################################

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/submit_order", methods=["POST"])
def order():
    # Get user input
    pizza_type = request.form["pizza_type"]
    pizza_size = request.form["pizza_size"]
    toppings = request.form.getlist("toppings")
    quantity = int(request.form["quantity"])

    # Calculate total price    
    price = calculate_price(pizza_size, pizza_type, toppings, quantity)
    
    name = request.form['name']
    phone = request.form['phone']
    credit_card_number = request.form['credit_card_number']
    credit_card_password = request.form['credit_card_password']
    address = request.form['address']

    # Display order confirmation
    return render_template("order.html", pizza_type=pizza_type, pizza_size=pizza_size, 
                            toppings=toppings, quantity=quantity, price=price,
                            name=name, phone=phone, 
                            credit_card_number=credit_card_number, 
                            credit_card_password=credit_card_password,
                            address=address)


if __name__ == '__main__':
    app.run(debug=True)