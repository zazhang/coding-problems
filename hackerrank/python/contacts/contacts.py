#!~/usr/bin/env ipython

""" Contacts (Tries)

Tries: a tree data structure that stores characters as nodes, and 
check weather the path forms a word.

The contacts application must perform two types of operations:

1. add name, where `name` is a string denoting a contact name. 
This must store `name` as a new contact in the application.
2. find partial, where `partial` is a string denoting a partial name 
to search the application for. It must count the number of contacts 
starting with `partial` and print the count on a new line.

"""

class Node():
   def __init__(self):
       """
       Note that using dictionary for children (as in this
       implementation) would not allow lexicographic sorting
       mentioned in the next section (Sorting),
       because ordinary dictionary would not preserve the order
       of the keys.
       """
       self.children = {}  # mapping from character ==> Node
       #self.value = None
       self.end = False
       self.size = 0

def find(node, key):
    """
    @param node: Node
    @param key: char
    @return string
    """
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return 0
    
    #result = []
    #traverse(node, list(key), result)
    #answer = [''.join(r) for r in result]
    #return len(answer)
    return node.size
    
def add(root, string):
    """
    @param root: Node
    @param string: str
    @return None
    """
    node = root
    i = 0
    while i < len(string):
        if string[i] in node.children:
            node = node.children[string[i]]
            node.size += 1
            i += 1
        else:
            break

    # append new nodes for the remaining characters, if any
    while i < len(string):
        node.children[string[i]] = Node()
        node = node.children[string[i]]
        node.size += 1
        i += 1
        
    # store value in the terminal node
    #node.value = value
    node.end = True

def traverse(node, partial, result):
    if node.end:
        result.append(partial[:])
    
    for char, n in node.children.items():
        partial.append(char)
        traverse(n, partial, result)
        partial.pop(-1)

        
if __name__ == '__main__':

    node = Node()
    """
    n = int(raw_input().strip())
    for a0 in xrange(n):
        op, contact = raw_input().strip().split(' ')
        if op == 'add':
            add(node, contact)
        if op == 'find':
            print find(node, contact)
    """
    """
    node = Node()
    add(node, 'hack', 'hack')
    add(node, 'hackerrank', 'hackerrank')
    answer = find(node, 'hac')
    print answer
    """

    # Read input from file
    filename = "input3.txt"
    filename2 = "output3.txt"
    with open( filename ) as f, open( filename2 ) as g:        
        content = f.readlines()
        result = g.readlines()
        n = [x.strip() for x in content[0]]
        n = int(''.join(n))
        content = [x.strip() for x in content[1:]]
        result = [y.strip() for y in result]
        temp = []
        for a0 in xrange(n):
            op, contact = content[a0].strip().split(' ')
            if op == 'add':
                add(node, contact)
            if op == 'find':
                #print find(node, contact) == int(result[a0/2])
                temp.append(find(node, contact) == int(result[a0/2]))
        print reduce(lambda x, y: x*y, temp)
