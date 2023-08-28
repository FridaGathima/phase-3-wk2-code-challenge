
class Review:
    all = []
    
    # review initialization
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all.append(self)

    # returns the rating for a restaurant
    def review_rating(self): #review_rating(self, rating)
        self.rating
    
    # returns all the reviews
    @classmethod
    def all(cls):
       return Review.all

    # returns the customer object for that review
    @property
    def customer(self):
        return self.customer
    
    #returns the restaurant object for that given review
    @property
    def restaurant(self):
        return self.restaurant
    
           
