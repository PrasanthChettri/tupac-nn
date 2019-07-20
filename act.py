import math
#ACTIVATION FUNCTION
class step :
    #f(x) : x>=1->1 else 0
    def f(x):
        return int(x >= 1)

class sigmoid :
    #Search sigmoid on the web
    def f(x):
        return  1/(1 + pow(math.e , -x))
