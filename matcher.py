


class Matcher():

    def __init__(self, origin = 'Padova', 
                 destination = 'all', 
                 date_start = 'today', 
                 date_finish = None,
                 felexibility_days = 0,
                 sort_by = 'cheapest'):
        self.origin = origin
        self.destination = destination
        self.date_start = date_start
        self.date_finish = date_finish
        self.felexibility_days = felexibility_days
        self.sort_by = sort_by

    def find_housing(self, results = 20, radius = 10):
        # sort available housing at destination by price and return the best `results` number of options
        
        housing_list = get_housing_solutions(self.destination, radius)

        return sorted(housing_list, key = lambda x: x.price)

    def find_transportation(self, results = 3):
        # sort best transportation means by price
        pass

    def match(self, results = 10):
        # find the best solutions for travel and show top results
        pass
        