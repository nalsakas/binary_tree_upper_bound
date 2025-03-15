import math

class Node:
    def __init__(self, val = None, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# For any given node, find nearest upper_bound
def upper_bound(src):
    bound = {
        'src': src.val,
        'upper': math.inf
    }

    visited = set()

    explore(src, bound, visited)
    return bound['upper']

def explore(src, bound, visited):
    if src is None:
        return
    
    if src in visited:
        return
    
    visited.add(src)

    if bound['src'] < src.val < bound['upper']:
        bound['upper'] = src.val

    explore(src.parent, bound, visited)   
    explore(src.left, bound, visited)
    explore(src.right, bound, visited)

if __name__ == "__main__":
    n20 = Node(20)
    n9 = Node(9)
    n25 = Node(25)
    n12 = Node(12)
    n5 = Node(5)
    n11 = Node(11)
    n14 = Node(14)

    root = n20
    n20.left = n9
    n20.right = n25
    n9.left = n5
    n9.right = n12
    n12.left = n11
    n12.right = n14

    n25.parent = n20
    n9.parent = n20
    n5.parent = n9
    n12.parent = n9
    n11.parent = n12
    n14.parent = n12

    assert upper_bound(root)  == 25
    assert upper_bound(n9) == 11 
    assert upper_bound(n11) == 12
    assert upper_bound(n25) == math.inf

    print(upper_bound(root))
    print(upper_bound(n9))
    print(upper_bound(n11))
    print(upper_bound(n25))