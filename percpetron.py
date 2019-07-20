import math
from random import randint
import numpy as np
import act
import loss
 

class perceptron:
    def __init__(self 
                 , inp, train = True, 
                 activation = act.sigmoid ,lr = 0.003 , 
                 Loss = loss.sample ):

        self.i_dim = inp
        self.weights = np.zeros((1, self.i_dim))
        self.bias = randint(1 , 5) 
        self.act = activation
        self.lr = lr
        self.Loss = Loss

    def assertions(self, inp):
        #SOME assertions
        assert inp.shape == self.weights.shape[::-1],"check the dimensions"
        ass_dt = inp.dtype == np.float64 or inp.dtype  == np.float32
        assert  ass_dt  , "the features should be float"

    def feed_forward(self, inp):
        #f(x, w, b) = output
        #d = g(x)(target)
        self.assertions(inp)
        output = np.matmul(self.weights , inp) + self.bias*1  
        return output

    def forward(self, feat, labels):
        output =  self.feed_forward(feat)
        output = self.act.f(output)
        loss = self.Loss.p(output , labels)
        return output ,loss

    def __repr__(self):
        return "Wuba luba DUB DUBS , amirite?"

if __name__ == '__main__':
    k = perceptron(inp = 3)
    target = [[1]]
    feat = np.array([[1.] , [2.], [3.]])# , dtype = np.float32)
    print (k.forward(feat, target))
