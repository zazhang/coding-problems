#!usr/bin/env ipython

"""Multiple Linear Regression (statistics)

Find coefficients for `y = 1*a + b1*x1 + b2*x2 + ...` using training set of data.
Find y values for the test set using the coefficients.

Multiple Linear Regression:
Y = X \dot B
X.transpose \dot Y = X.transpose \dot X \dot B
(X.transpose \dot X).inverse \dot X.transpose \dot Y = Identity \dot B
B = (X.transpose \dot X).inverse \dot X.transpose \dot Y

"""

import numpy as np


class Solution(object):
    def multipleLinearReg(self, X, Y):
        """
        @param X: a numpy.matrix of float, representing X values
        @param Y: a list of float, representing Y values
        @return a numpy.matrix of float denoting regression coefficients
        """
        X = np.matrix(X)
        Y = np.matrix(Y)
        n = X.shape[0]
        m = X.shape[1]
        X_trans = X.T
        X_trans_X_inverse = (X_trans * X).I
        B = X_trans_X_inverse * X_trans * Y
        return B
        

if __name__ == '__main__':

    s = Solution()

    m,n = [int(i) for i in raw_input().strip().split(' ')]
    X = []
    Y = []
    for i in range(n):
        data = raw_input().strip().split(' ')
        data = ['1.0'] + data # add 1.0 to X, Y = 1*a + b1*x1 + b2*x2
        X.append(data[:m+1])
        Y.append(data[m+1:])
    q = int(raw_input().strip())
    X_new = []
    for x in range(q):
        data = ['1.0'] + data
        X_new.append(data) 
    X = np.array(X,float)
    Y = np.array(Y,float)
    X_new = np.array(X_new,float)

    b = s.multipleLinearReg(X,Y)
    res = (X_new * b).tolist()
    for i in xrange(len(res)):
        print round(res[i][0],2)

    # hard-coded test
    #x = np.matrix('1.0,0.18,0.89;1.0, 1.0, 0.26; 1.0,0.92, 0.11;1.0,0.07, 0.37;1.0,0.85, 0.16;1.0,0.99, 0.41; 1.0,0.87, 0.47 ')
    #y = np.matrix('109.85;155.72;137.66;76.17;139.75;162.6;151.77')
    #test = np.matrix('1.0,0.49 0.18;1.0,0.57, 0.83;1.0,0.56, 0.64;1.0,0.76, 0.18 ')
    #b = s.multipleLinearReg(x,y)
    #res = test * b
    #print res    