class Coffee:
    def __init__(self, name):
        # if type(name) is str and 3<=len(name):
        self.name = name
    
    def get_name(self):
        return self._name
    def set_name(self,value):
        if not hasattr(self,"name") and type(value) is str and 3<=len(value):
            self._name = value
        else:
            raise ValueError("Not valid name")
    name = property(get_name,set_name)
    
    def orders(self):
        r_list = []
        for order in Order.all:
            if type(order) is Order and order.coffee is self:
                r_list.append(order)
        return r_list
    
    def customers(self):
        r_list = []
        for order in Order.all:
            if order.coffee is self and type(order.customer) is Customer and order.customer not in r_list:
                r_list.append(order.customer)
        return r_list
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee is self:
                count += 1
        return count
    
    def average_price(self):
        count = 0
        sum = 0
        for order in Order.all:
            if order.coffee is self:
                count += 1
                sum += order.price
        if count == 0:
            return 0
        return sum/count

class Customer:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else:
            raise ValueError("Not valid name")
    name = property(get_name,set_name)

    def orders(self):
        r_list = []
        for order in Order.all:
            if type(order) is Order and order.customer is self:
                r_list.append(order)
        return r_list
    
    def coffees(self):
        r_list = []
        for order in Order.all:
            if order.customer is self and type(order.coffee) is Coffee and order.coffee not in r_list:
                r_list.append(order.coffee)
        return r_list
    
    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    def set_price(self,value):
        if isinstance(value,float) and 1.0<=value<=10.0 and not hasattr(self,"price"):
            self._price=value
        else:
            raise ValueError("Not valid price")
    price = property(get_price,set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self, value):
        if type(value) is Customer:
            self._customer = value
        else:
            raise ValueError("Not valid customer")
    customer = property(get_customer,set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self, value):
        if type(value) is Coffee:
            self._coffee = value
        else:
            raise ValueError("Not valid coffee")
    coffee = property(get_coffee,set_coffee)

    

cappaccino = Coffee("Cappaccino")
americano = Coffee("Americano")
black = Coffee("Black")

tri = Customer("Tri")
baran = Customer("Baran")
jake = Customer("Jake")

Order(tri,black,2.5)
Order(tri,black,3.0)
Order(baran,black,2.5)
Order(baran,americano,5.0)
Order(jake,cappaccino,4.0)

# print(black.customers())
baran.create_order(cappaccino,6.0)
# print(baran.coffees())
# print(baran.orders())
# print(americano.num_orders())
print(americano.average_price())