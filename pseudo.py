from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.val)
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.val)
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.val)

    def find(self, val) -> bool:
        if val < self.val:
            if self.left is None:
                return False
            else:
                return self.left.find(val)
        elif val > self.val:
            if self.right is None:
                return False
            else:
                return self.right.find(val)
        else:
            return True


tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

tree.inOrderTraversal()
print()
tree.preOrderTraversal()
print()
tree.postOrderTraversal()
print()
print(tree.find(3))
print()


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val


tree = TreeNode(2)
tree.insert(1)
tree.insert(3)
print(Solution().findBottomLeftValue(tree))
