import json
class Car:

    def __init__(self,id,make,model,year,price,vin, is_sold=False):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.vin = vin
        self.is_sold = is_sold

    def display(self):
        status = "Sold" if self.is_sold else "Available"
        print(f"{self.id}: {self.year} {self.make} {self.model} ${self.price} {status}")
        
def save_inventory(): 
    with open("cars.json", "w") as file:
        json.dump([car.__dict__ for car in inventory],file, indent=4)

def load_inventory(): 
    global inventory
    try: 
        with open("cars.json","r") as file:
            data = json.load(file)
            inventory = [Car(**car) for car in data]
    except FileNotFoundError:
        inventory = []
def addcar():
    id = (len(inventory) + 1)
    make = input("Enter the cars make: ")
    model = input("Enter the cars model: ")
    year = int(input("Enter the cars year: "))
    price = int(input("Enter the cars price: "))
    vin = input("Enter the cars vin: ")

    new_car = Car(id,make,model,year,price,vin)

    print("Car has been added to the inventory!\n")
    inventory.append(new_car)
    save_inventory()
    new_car.display()

def listinventory():
    if len(inventory) == 0:
        print("You have no cars in your inventory")
    else:
        print("--------- Car Inventory --------")
        for car in inventory:
            car.display()
        
        print('--------------')
        filterask = input("Type F to filter the results: ")
        print()
        if filterask not in "F":
            return
        else: filter()

def filter():
    print("Choose how you would like to filter the results: ")
    choice = input("Please pick one of the options below: \n Y to Filter by year  \n C to display only specific priced cars \n M to search for specific make \n Any other letter to quit: ")
    if choice in ('Y','C','M'):
        if choice == "Y":
            displayyear()
        if choice == "C":
            displayprice()
        if choice == "M":
            displaymake()

def displayyear():
    min = input("Please enter the oldest year: ")
    max = input("Please enter the newest year: ")
    removed = 0
    for car in inventory:
        if min <= car.year <= max:
            car.display()
        else:
            removed += 1
    print(f"{removed} cars have been removed from the list")

def displayprice():
    min = int(input("Please enter the lowest price:  "))
    max = int(input("Please enter the highest price: "))
    removed = 0
    for car in inventory:
        if int(car.price) >= min and int(car.price) <= max:
            car.display()
        else:
            removed += 1
    print(f"{removed} cars have been removed from the list")

def displaymake():
    make = input("Please enter the make your looking for:  ")
    removed = 0
    for car in inventory:
        if car.make in make:
            car.display()
        else:
            removed += 1
    print(f"{removed} cars have been removed from the list")
        


    
def main():
    print('-----------WELCOME TO FBs DEALERSHIP---------')
    select = input(('-----Press enter to head to the main menu-------(q to quit):'))
    while select.lower != 'q':
        print()
        select = input("--------Options:--------\nI for inventory\nA to add a car\nPlease select one:")
        if select.lower == "q":
            return
        while select not in ('I','A','Q'):
            print("That is not a valid option. Please select from the options listed.")
            select = input("Options:\nI for inventory\nA to add a car\n Please select one:")

        if select == "I":
            listinventory()
        elif select == "A":
            addcar()
        elif select == "Q":
            break
        

    
inventory = []
load_inventory()

main()