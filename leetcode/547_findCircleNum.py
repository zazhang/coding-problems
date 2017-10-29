#!usr/bin/env ipython

"""Coding interview problem (graphs): 

There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend 
of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or 
indirect friends.

Given a N*N matrix M representing the friend relationship between students 
in the class. If M[i][j] = 1, then the ith and jth students are direct friends 
with each other, otherwise not. And you have to output the total number of 
friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2

"""

visited = set() # create a global variable to store visited nodes
class Solution(object):
    def findCircleNum(self, M):
        """This is an iterative implementation using a global variable.
        :type M: List[List[str]]
        :rtype: int
        :notes: This problem is using a visited set to keep tracking 
                all the nodes that have been visited through dfs. If
                dfs can visit all nodes at once, meaning only one 
                circle is existed. So everytime dfs is executed, we
                increment the counter by one.
        """
        cnt = 0
        for i in xrange(len(M)):
            if i not in visited:
                self.dfs(M, i)
                cnt += 1
        return cnt

    def dfs(self, g, v):
        """
        @param g : a 2d array representing the adjacency matrix
        @param v: a starting vertex in g
        @return all connected vertices of v
        """
        s = [v]
        while s != []:
            vertex = s.pop()
            if vertex not in visited:
                visited.add(vertex)
                for i in xrange(len(g[vertex])): # find the node number of any edge
                    if g[vertex][i] != 0:
                        s.append(i)
        return visited
        
    def findCircleNum2(self, A):
        """This is a recursive answer implementation.
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in xrange(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans

    def findCircleNum3(self, M):
        """This is an iterative answer implementation.
        :type M: List[List[int]]
        :rtype: int
        """        
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j,v in enumerate(M[cur]) if v and j not in seen] + toSee
                res += 1
        return res

    def findCircleNum4(self, M):
        """This is an iterative implementation without using global variable.
        :type M: List[List[int]]
        :rtype: int
        """            
        visit = set()
        cnt = 0

        for v in xrange(len(M)):
            if v not in visit:
                s = [v]
                while s != []:
                    vertex = s.pop()
                    if vertex not in visit:
                        visit.add(vertex)
                        # find the node number of any edge
                        for i in xrange(len(M[vertex])): 
                            if M[vertex][i] != 0:
                                s.append(i)
                cnt += 1
        return cnt


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = [[1,0,0],[0,1,0],[0,0,1]]
    print s.findCircleNum4(A)
