class MenuItem:
    # food menu 
    def __init__(self, name, price):
        self.name=name
        self.price=price
    

    def __str__(self):
        return "{} Price: {}".format(self.name,self.price)
    

# menu instance create
burger = MenuItem("Hambuger", 4000)
coke = MenuItem("Coke", 1500)
fries = MenuItem("French fries", 1500)

# menu instance print
print(burger)
print(coke)
print(fries)