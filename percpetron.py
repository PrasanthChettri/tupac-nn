import math
import numpy as np
import act
from random import randint
 

class perceptron:
    def __init__(self , inp, train = True, activation = act.sigmoid , lr = 0.003):
        self.i_dim = inp
        self.weights = np.zeros((1, self.i_dim))
        self.bias = randint(1 , 5) 
        self.act = activation
        self.lr = lr

    def feed_forward(self, inp):
        #SOME assertions
        assert inp.shape == self.weights.shape[::-1],"check the dimensions"
        ass_dt = inp.dtype == np.float64 or inp.dtype  == np.float32
        assert  ass_dt  , "the features should be float"
        output = np.matmul(self.weights , inp) + self.bias*1  
        return output

    def forward(self, feat, labels):
        output =  self.feed_forward(feat)
        output = self.act.f(output)
        loss = None
        return output ,loss

    def performance_check(self, output, target):
        pass

    def optimizer(self):
        pass

    def __repr__(self):
        return "Wuba luba DUB DUBS , amirite?"

if __name__ == '__main__':
    k = perceptron(inp = 3)
    target = [[1]]
    feat = np.array([[1.] , [2.], [3.]])# , dtype = np.float32)
    print (k.forward(feat, target))
