#!usr/bin/env ipython

"""Left Rotation (array)

A left rotation operation on an array of size `n` shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array of `n` integers and a number, `d`, perform `d` left rotations on the array. Then print the updated array as a single line of space-separated integers.

"""


def array_left_rotation(a, n, k):
    """
    @param a : a list of int
    @param n : int indicating length of `a`
    @param k : int indicating the number of position to rotate
    @return a list of int
    """
    ret = []
    move = k % n
    for i in xrange(n):
    	if (i+move) >= n:
    		ret.append(a[i + move - n])
    	else:
    		ret.append(a[i + move])
    return ret
    

if __name__ == '__main__':
         
    # Read input from prompt
	n, k = map(int, raw_input().strip().split(' '))
	a = map(int, raw_input().strip().split(' '))
	answer = array_left_rotation(a, n, k);
	print ' '.join(map(str,answer))    
        
    """
   	# Read input from file
    filename = "input1.txt"
    with open( filename ) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        #print content
        n, k = map(content[1].strip().split(' '))
        a = map(content[2].strip().split(' '))
        answer = array_left_rotation(a, n, k)
        print ' '.join(map(str,answer)) 
    """
