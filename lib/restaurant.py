from review import Review


class Restaurant(Review):
    # restaurant initialization
    def __init__(self, name): # def __init__(self, restaurant_name)
        self.name = name
       
    @property
    def name(self):
        return self.name
       
    #returns a list of all reviews for that restaurant
    def reviews(self):
        reviews = Review.all
        return [rev for rev in reviews if rev.restaurant.name == self.name]

    # Returns a **unique** list of all customers who have reviewed a particular restaurant.
    def customers(self):
        review = Review.all
        return list({rev.customer for rev in review if rev.restaurant.name == self.name })
    
    # returns the average star rating for a restaurant based on its reviews

    def restaurant_average_star_rating():
        rating_sum = 0
        for review in Review.all:
            rating_sum += review.rating
            return (rating_sum / len(Review.all))
