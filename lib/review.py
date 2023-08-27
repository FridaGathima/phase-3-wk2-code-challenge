
class Review:
    # review initialization
    def __init__(self, customer, restaurant_name, rating):
        self.customer = customer
        self.restaurant_name = restaurant_name
        self.rating = rating 

    # returns the rating for a restaurant
    def review_rating(self, rating):
        #  if rating == int(rating) or rating == float(rating):  
        #     print (rating)
        if self.rating == int(self.rating) or self.rating == float(self.rating):  
            return self.rating
        else:
            print ("rating must be a number")
        self.rating = rating 
    
    # returns all the reviews
    def review_all(self, customer, restaurant_name, rating):
        print(f"{self.customer} {self.restaurant_name} {self.rating}")
        self.customer = customer
        self.restaurant_name = restaurant_name
        self.rating = rating 
        # should i return only the rating no?

    # returns the customer object for that review
    def review_customer(self, rating):
        self.rating = rating
        return self.customer
           
    # def review_customer(self, customer, rating):
    #     super().customer_all(self)
    #     print (f"{self.rating} {self.customer}")
    #     self.rating = rating 
    #     self.customer = customer
    
    #returns the customer object for that review
    def review_restaurant(self, rating):
        self.rating = rating
        return self.restaurant_name
        # super().RESTAURANT_NAME(self)
        # self.rating = rating 
        # return self.restaurant_name

    # review_restaurant(4)
    # review_rating("12", "hello")