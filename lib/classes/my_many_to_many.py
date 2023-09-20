class Coffee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, 'name'):
            self._name = name
        else:
            print('This is not a valid name.')

    name = property(get_name, set_name)    
    
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) and len(name) <= 15:
            self._name = name
        else:
            print('This is not a valid name.')
  
    name = property(get_name, set_name)   
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if isinstance(price, float) and 1.0 <= price and price <= 10.0 and not hasattr(self, 'price'):
            self._price = price
        else:
            print('This is not a valid input.')
  
    price = property(get_price, set_price) 

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else: 
            print ('This is not a valid customer.')

    customer = property(get_customer, set_customer)

