class Wallet:
    def __init__(self, money=0):
        self.money =money 

    def credit(self,amount):
        self.money=self.money+amount
       # print(amount+ self.money)

    def debit(self,amount):
         self.money=self.money-amount
       # print(amount+ self.money)
    def __str__(self):
        return f"the amount {self.money} "

wallet = Wallet(6)
print(wallet )
# wallet = Wallet()  # This should default money inside the wallet to 0
# print(wallet)


class Person:
    # Implement the code here
     def __init__(self, name,location ,money):
        
        self.name=name
        self.location=location
        self.wallet=Wallet(money)
     def moveTo(self,point):
        self.location=point


     def __str__(self):
        return f"the location {self.location} "

person = Person("Moh", 5, 50)
print(person)

class Vendor(Person):
    # implement Vendor!
     def __init__(self, name,location,money):
        super().__init__( name,location ,money)
        self.range=5
        self.price=1
        
     def sellTo(self,customer, number_of_icecreams):
        self.location = customer.location
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)
        


vendor = Vendor("Abdallah", 3, 6)
print(vendor)


class Customer(Person):
#     # implement Customer!

   def __init__(self, name,location,money):
        super().__init__( name,location ,money)
    
    
   def _is_in_range(self,vendor):
     check_range=vendor.location -self.location
     if check_range > vendor.range:
      print("the customer is in range")
      return True
     else:
      print("the customer is out range")
      return False
   def _have_enough_money(self,vendor, number_of_icecreams):
     if self.wallet.money >= number_of_icecreams*vendor.price:
       print("u have enough money ")
       return True
     else:
       print("u don't have enough money ")
       return False
   def request_icecream(self,endor, number_of_icecreams): 
      if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecreams):
            vendor.sellTo(self, number_of_icecreams)

vendor_aziz = Vendor(
    "Asis", 10, 10
)  # create a new vendor named Asis at location 10 with a money value of 10
nearby_customer = Customer(
    "MishMish", 11, 10
)  # create a new customer named MishMish at location 11 with a money value of 10
distant_customer = Customer(
    "Hamsa", 1000, 1000
)  # create a new customer named Hamsa at location 1000 with a money value of 10
broke_customer = Customer(
    "Maskeen", 12, 0
)  # create a new customer named Maskeen at location 12 with 0 money


nearby_customer.request_icecream(vendor_aziz, 10)  # ask to buy 10 ice creams from Asis
# money was transferred from MishMish to Asis
print(nearby_customer.wallet.money)  # 0 left
print(vendor_aziz.wallet.money)  # 10
# Asis moved to MishMish's location
print(vendor_aziz.location)  # 11

distant_customer.request_icecream(vendor_aziz, 10)  # ask to buy 10 ice creams from Asis
# no money was transferred because the request failed - Hamsa is too far away
print(distant_customer.wallet.money)  # 10 left
print(vendor_aziz.wallet.money)  # still only 10
# Asis didn't move
print(vendor_aziz.location)  # 11

broke_customer.request_icecream(vendor_aziz, 1)  # ask to buy 1 ice creams from Asis
# no money was transferred because the request failed - Maskeen doesn't have enough money to buy even one ice cream :(
print(broke_customer.wallet.money)  # 0
print(vendor_aziz.wallet.money)  # still only 10
# Asis didn't move
print(vendor_aziz.location)  # { x: 11, y: 11 }