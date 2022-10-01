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
