from review import Review


class Restaurant(Review):
    # restaurant initialization
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        # super().review_all()
        # # self.rating = rating
    
    # returns restaurant name
    def RESTAURANT_NAME(self):
        #shouldnt change put caps
        return self.restaurant_name
        # print (RESTAURANT_NAME("a"))
       
    #returns a list of all reviews for that restaurant
    def restaurant_reviews(self, restaurant_name):
        super().review_rating()
        self.restaurant_name = restaurant_name
        return self.rating
    #     # should return review_rating() from reviews
    #     return ("res")

    # Returns a **unique** list of all customers who have reviewed a particular restaurant.
    def restaurant_customers():
        pass
    
