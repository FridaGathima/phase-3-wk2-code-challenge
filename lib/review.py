from customer import Customer
from restaurant import Restaurant


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating 

    def review_rating(rating, restaurant):
        #  if self.rating == int(self.rating) or self.rating == float(self.rating):  
        #     print (self.rating)
        if rating == int(rating) or rating == float(rating):  
            print (rating)
        else:
            print ("rating must be a number")
        print (restaurant)
        
    def review_all(customer, restaurant, rating):
        print( print(f"{customer} {restaurant} {rating}"))
        # should i return only the rating no?


    # importing customer details for a certain review

    def review_customer(Customer, rating):
        print (rating)
        
    
    #returning the restaurant 

    def review_restaurant(rating):
        print (Restaurant)

    review_restaurant(4)
    # review_rating("12", "hello")