#!usr/bin/env ipython

"""Linear Regression (statistics)

A group of five students enrolls in Statistics immediately after taking a 
Math aptitude test. Each student's Math aptitude test score, x, and 
Statistics course grade, y, can be expressed as the following 
list of (x,y) points:

    (95, 85)
    (85,95) 
    (80, 70)
    (70,65) 
    (60,70)

If a student scored an 80 on the Math aptitude test, what grade would we 
expect them to achieve in Statistics? Determine the equation of 
the best-fit line using the least squares method, then compute and print 
the value of y when x=80.

"""


class Solution(object):
    def linearReg(self, A):
        """
        @param A: a list of 2-tuple of int
        @return a list of float denoting the slope and intercept of the
            linear regression
        """
        X = [e[0] for e in A]
        Y = [e[1] for e in A]
        n = len(A)
        sum_x = sum(X)
        sum_y = sum(Y)
        avg_x = sum_x / n
        avg_y = sum_y / n
        x_square = sum([x*x for x in X])
        #print 'x_square %s' %x_square
        xy = sum([X[i]*Y[i] for i in xrange(n)])
        #print 'xy %s' %xy

        slope = (n*xy - sum_x*sum_y) / (n*x_square - sum_x**2.0)
        intercept = avg_y - slope * avg_x
        #print '(slope, intercept) ({0},{1})'.format(slope,intercept)

        return [slope, intercept]
        

if __name__ == '__main__':

    s = Solution()

    d = [(95, 85), (85,95), (80, 70), (70,65), (60,70)]
    d2 = [(1,2),(2,1),(3,4),(4,3),(5,5)]
    lin = s.linearReg(d)
    res = 80*lin[0]+lin[1]
    print round(res, 3)
