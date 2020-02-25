# Definition for a binary tree node.
class Node:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def __init__(self):
    self.hashMap = {}
    self.max = 0

  # time O(N), memory O(N)
  def calcHash(self, node: Node):
    if node == None:
      return 0

    # Each node have left and right child max length
    self.hashMap[node] = {'left': 0, 'right': 0}

    if node.left is not None:
      # Adding +1 after calling
      maxLeftNode = self.calcHash(node.left) + 1

      # After calling self.calcHash we need to check,
      # if current value more then current value (self.hashMap[node]['left'])
      if self.hashMap[node]['left'] < maxLeftNode:
        self.hashMap[node]['left'] = maxLeftNode

    if node.right is not None:
      # Adding +1 after calling
      maxRightNode = self.calcHash(node.right) + 1

      # After calling self.calcHash we need to check,
      # if current value more then current value (self.hashMap[node]['right'])
      if self.hashMap[node]['right'] < maxRightNode:
        self.hashMap[node]['right'] = maxRightNode

    # Check max sum
    if self.hashMap[node]['left'] + self.hashMap[node]['right'] > self.max:
      self.max = self.hashMap[node]['left'] + self.hashMap[node]['right']

    # return max child length in left or right child
    return max(self.hashMap[node]['left'], self.hashMap[node]['right'])

  def diameterOfBinaryTree(self, root: Node) -> int:

    self.calcHash(root)

    return self.max


# my = Solution()

t0 = Node(1, Node(2, Node(4), Node(5)), Node(3))

ans = my.diameterOfBinaryTree(t0)
print('ans %d' % ans)

# Runtime: 36 ms, faster than 96.52% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.