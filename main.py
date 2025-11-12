class Car:

    def __init__(self,id,make,model,year,price,vin):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.vin = vin
        self.is_sold = False

    def display(self):
        status = "Sold" if self.is_sold else "Available"
        print(f"{self.id}: {self.year} {self.make} {self.model} ${self.price} {status}")
        
    
def addcar():
    id = (len(inventory) + 1)
    make = input("Enter the cars make: ")
    model = input("Enter the cars model: ")
    year = input("Enter the cars year: ")
    price = input("Enter the cars price: ")
    vin = input("Enter the cars vin: ")

    new_car = Car(id,make,model,year,price,vin)

    print("Car has been added to the inventory!\n")
    inventory.append(new_car)
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
    choice = input("Please pick one of the options below: \n Y to Filter by year  \n C to display only cheap cars \n M to search for specific make \n Any other letter to quit: ")
    if choice in ('Y','C','M'):
        if choice == "Y":
            displayyear()
        if choice == "C":
            displayprice()
        if choice == "M":
            pass

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
    min = input("Please enter the lowest price:  ")
    max = input("Please enter the highest price: ")
    removed = 0
    for car in inventory:
        if min <= car.price <= max:
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
    while select not in'q':
        print()
        select = input("--------Options:--------\nI for inventory\nA to add a car\nPlease select one:")
        while select not in ('I','A'):
            print("That is not a valid option. Please select from the options listed.")
            select = input("Options:\nI for inventory\nA to add a car\n Please select one:")

        if select == "I":
            listinventory()
        if select == "A":
            addcar()
    
inventory = []

main()