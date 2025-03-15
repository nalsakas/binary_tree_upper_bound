# binary_tree_upper_bound
Find upper bound for a given node in a binary tree.

# Problen Statement:
For a given binary tree that contains numbers find upper boud for a given node.
Upper bound is smallest node value bigger than current node.

Example:
```
    20
     |
   9  25
   |
5     12
       |
    11   14
``` 
# Solution:
- Use dfs algorithm to explore tree
- Set default upper bound to math.inf
- When a value bigger than current value but less than upper appears replace upper bound with that one.