#loss function I found in the mit ML opencourseware 
#I don't know what it's called
class sample:
    #p(x)->-(||y-z||)^2
    def p(y, z):
        return -abs(y-z)**2
