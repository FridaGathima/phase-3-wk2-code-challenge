from review import Review


class Customer(Review):
    # customer initialization
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        # Review.__init__(self, customer, restaurant_name, rating)
    
    # returns customer given_name
    def customer_given_name(self):
        return self.given_name
    
    # returns customer family_name
    def customer_family_name(self):
        return self.family_name
    
    # returns customer full name        
    def customer_full_name(self, given_name, family_name):
        print(f"{given_name} {family_name}")
        self.given_name = given_name
        self.family_name = family_name
    
    # returns all instances of the customer
    def customer_all(self):
        # return self # still not sure what to include
        return "hello customer all test"
        pass

    # Returns a **unique** list of all restaurants a customer has reviewed
    def customer_restaurants(self):
        super().review_customer()
        pass

    # given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
    def customer_add_review(restaurant_name, rating):
        if rating == int(rating):  
            return f"{rating} {customer} {restaurant_name}"
        else:
            print ("rating must be a number") 

    
    


    

    




# mary = Customer("Mary", "Smith")

# print (Customerfamily_name)