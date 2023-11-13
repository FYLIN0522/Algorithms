"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
##from bitarray import bitarray
import re
from heapq import *

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)
        
        self.result = []


    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False


    def traversal(self, a, res=[]): 
        if a.is_leaf() is True:
            self.result += [(''.join(res), a.char)]
            return 

        self.traversal(a.left, res + ['0'])
        self.traversal(a.right, res + ['1'])



    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

        
    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        encode = ''
        root = self.root
        if root.is_leaf() is False:
            root.traversal(root)
##            print(root.result)
            for i in text:
                for j in root.result:
                    if i in j:
                        encode += j[0]
                        break

        elif root.is_leaf() is True:
            return encode
                
        return encode

            


        
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        root = self.root
        code = ''

        for i in binary:
            if i == '0':
                root = root.left             
                
            elif i == '1':
                root = root.right
                
            if root.is_leaf():
                code += root.char
                root = self.root

                
        return code
                
        raise NotImplementedError  # *** TO BE IMPLEMENTED


    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
##                node_list.pop(0)
##                print(node_list[0])
##                node_list.insert(0, [Node(node_list[0], Leaf(freqs[1][1], freqs[1][0])), node_list[0][1] + freqs[1][1]])
##                print(node_list)
        """Define self.root to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None          # *** FIXME ***
##        trees = []
##
##        for key in freqs.keys():
##            val = freqs[key]
##            heappush(trees, Leaf(val, key))
##
##        while len(trees) > 1:
##            left = heappop(trees)
##            right = heappop(trees)
##            total_count = left.count + right.count
##            heappush(trees, Node(total_count, left, right))
##
##        self.root = heappop(trees)

        
        if len(freqs) == 1:
            for i, j in freqs.items():
                self.root = Leaf(j,i)
            return self.root

        
        node_list = []
        freqs = sorted(freqs.items(), key=lambda item:item[1])
##        print(freqs[0][0])

        while len(freqs) > 1:    
            if freqs[0][0] != 'node' and freqs[1][0] != 'node':
                if freqs[0][1] == freqs[1][1]:
                    s = freqs[:2]
                    s = sorted(s, key=lambda s:s[0])
                    self.root = Node(Leaf(s[0][1], s[0][0]), Leaf(s[1][1], s[1][0]))              
                    node_list += [((Node(Leaf(s[0][1], s[0][0]), Leaf(s[1][1], s[1][0])), s[0][1] + s[1][1]))]
                    
                else:     
                    self.root = Node(Leaf(freqs[0][1], freqs[0][0]), Leaf(freqs[1][1], freqs[1][0]))              
                    node_list += [((Node(Leaf(freqs[0][1], freqs[0][0]), Leaf(freqs[1][1], freqs[1][0])), freqs[0][1] + freqs[1][1]))]



                
            elif freqs[0][0] == 'node' and freqs[1][0] != 'node':
                node_list = sorted(node_list, key=lambda value:value[1])
                if node_list[0][1] == freqs[1][1]:
                    if node_list[0][0].min_char < freqs[1][0]:
                        self.root = Node(node_list[0][0], Leaf(freqs[1][1], freqs[1][0]))
                        node_list[0] = [Node(node_list[0][0], Leaf(freqs[1][1], freqs[1][0])), node_list[0][1] + freqs[1][1]]
                                        
                    else:
                        self.root = Node(Leaf(freqs[1][1], freqs[1][0]), node_list[0][0])
                        node_list[0] = [Node(Leaf(freqs[1][1], freqs[1][0]), node_list[0][0]), node_list[0][1] + freqs[1][1]]



                        
                elif node_list[0][1] < freqs[1][1]:
                    self.root = Node(node_list[0][0], Leaf(freqs[1][1], freqs[1][0]))
                    node_list[0] = [Node(node_list[0][0], Leaf(freqs[1][1], freqs[1][0])), node_list[0][1] + freqs[1][1]]
                else:
                    self.root = Node(Leaf(freqs[1][1], freqs[1][0]), node_list[0][0])
                    node_list[0] = [Node(Leaf(freqs[1][1], freqs[1][0]), node_list[0][0]), node_list[0][1] + freqs[1][1]]
                


            elif freqs[0][0] != 'node' and freqs[1][0] == 'node':
                node_list = sorted(node_list, key=lambda value:value[1])
                if node_list[0][1] == freqs[0][1]:
                    if node_list[0][0].min_char < freqs[0][0]:
                        self.root = Node(node_list[0][0], Leaf(freqs[0][1], freqs[0][0]))
                        node_list[0] = [Node(node_list[0][0], Leaf(freqs[0][1], freqs[0][0])), node_list[0][1] + freqs[0][1]]
                    else:
                        self.root = Node(Leaf(freqs[0][1], freqs[0][0]), node_list[0][0])
                        node_list[0] = [Node(Leaf(freqs[0][1], freqs[0][0]), node_list[0][0]), node_list[0][1] + freqs[0][1]]


                
                elif node_list[0][1] < freqs[0][1]:
                    self.root = Node(node_list[0][0], Leaf(freqs[0][1], freqs[0][0]))
                    node_list[0] = [Node(node_list[0][0], Leaf(freqs[0][1], freqs[0][0])), node_list[0][1] + freqs[0][1]]
                else:
                    self.root = Node(Leaf(freqs[0][1], freqs[0][0]), node_list[0][0])
                    node_list[0] = [Node(Leaf(freqs[0][1], freqs[0][0]), node_list[0][0]), node_list[0][1] + freqs[0][1]]



            elif freqs[0][0] == 'node' and freqs[1][0] == 'node':
                node_list = sorted(node_list, key=lambda value:value[1])
                self.root = Node(node_list[0][0], node_list[1][0])

            
            i = freqs.pop(0)
            j = freqs.pop(0) 
            freqs.insert(0, ('node', i[1] + j[1]))
            freqs = sorted(freqs, key=lambda item:item[1])  
            print(freqs)

                
        return self.root

        raise NotImplementedError # *** TO BE IMPLEMENTED

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


        
##freqs = {'p': 27,
##         'q': 11,
##         'r': 27,
##         'u': 8,
##         't': 5,
##         's': 3}
##tree = HuffmanTree()
##tree.build_from_freqs(freqs)
##print(tree)


#### The example from the notes
freqs = {'a': 9,
         'b': 8,
         'c': 15,
         'd': 3,
         'e': 5,
         'f': 2}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)


##tree = HuffmanTree(Node(
##Node(
##Leaf(8, 'b'),
##Leaf(9, 'a')),
##Node(
##Node(
##Node(
##Leaf(2, 'f'),
##Leaf(3, 'd')),
##Leaf(5, 'e')),
##Leaf(15, 'c'))))
##print(tree.encode('adcb'))

# An easy base case
##tree = HuffmanTree(Node(Leaf(1, 'x'), Leaf(1, 'y')))
##print(tree.encode('xy'))
##print(tree.encode('xyxxyyxxxyyyxxxxyyyy'))

	
# A tricky base case. With an alphabet of only 1 character
# there is no information in a string, so the encoded string
# is empty.
##tree = HuffmanTree(Leaf(1, 'x'))
##print(tree.encode('xxxxxx'))

def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    tree = HuffmanTree()
    tree_string = """Node(42,
      Node(17,
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(25,
        Node(10,
          Node(5,
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c')))
    """
    freqs = {'p': 27,
             'q': 11,
             'r': 27,
             'u': 8,
             't': 5,
             's': 3}
    tree = HuffmanTree()
    tree.build_from_freqs(freqs)
##    tree.build_from_string(tree_string)
##    print(tree)
    tree.plot()
    
##    # Or you can build the tree directly
##    tree2 = HuffmanTree(Node(
##      Node(
##        Leaf(8, 'b'),
##        Leaf(9, 'a')),
##      Node(
##        Node(
##          Node(
##            Leaf(2, 'f'),
##            Leaf(3, 'd')),
##          Leaf(5, 'e')),
##        Leaf(15, 'c'))))
##    print(tree2)
##    tree2.plot()
    
main()



##import matplotlib.pyplot as plt
##from graphviz import Graph
##
### First some simple text output.
##vertices = [(0, 0), (100, 0), (1, 50), (100, 100), (0, 100), (0,0)]
##vx, vy = zip(*vertices)  # Unpack them
##points = [(1, 1), (20, 20), (20, 80), (60, 50),
##     (97, 1), (1, 48), (1, 52), (97, 99), (1, 99)]
##px, py = zip(*points) # Unpack
##print("Vertex x values:", vx)
##print("Vertex y values:", vy)
##print("Point x values:", px)
##print("Point y values:", py)
##
### Now a matplotlib graph.
##axes = plt.axes()
##axes.plot(vx, vy, color='blue', marker='o', linestyle='--')
##axes.plot(px, py, color='red', marker='x', linestyle='')
##axes.set_title('The example from the geometry lecture notes')
##
### Lastly a graphviz example
##g = Graph()
##g.node('Root', '23')
##g.node('Leaf1', '13', shape='box')
##g.node('Leaf2', '99', shape='box')
##g.edge('Root', 'Leaf1')
##g.edge('Root', 'Leaf2')
##g.render('graph', format='png', view=False)
