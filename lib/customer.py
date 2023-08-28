from review import Review

class Customer(Review):
    all = []
    # customer initialization
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all.append(self)
    
    # returns customer given_name
    @property
    def given_name(self): 
        return self.given_name
    
    # returns customer family_name
    @property
    def family_name(self): 
        return self.family_name
    
    # returns customer full name 
    @property       
    def full_name(self, given_name, family_name): 
        print(f"{given_name} {family_name}")
    
    # returns all instances of the customer
    def customer_all(self):
        return Customer.all

    # Returns a **unique** list of all restaurants a customer has reviewed
    def restaurants(self):
        return list({rev.restaurant for rev in Review.all if rev.customer.full_name == self.full_name})
        # super().review_customer()
        

    # given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
    def add_review(self, restaurant, rating):
        Review(self, restaurant=restaurant, rating=rating)

    # Returns the total number of reviews that a customer has authored
    def num_reviews(self):
        return len([review for review in Review.all if review.customer.fullname == self.full_name])

    # given a string of a **full name**, returns the **first customer** whose full name matches
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customer:
            if customer.full_name == name:
                return customer
            
    # given a string of a given name, returns an **list** containing all customers with that given name
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer.given_name for customer in cls.customers if customer.given_name == name]