
class TreeNode(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    def insert(node, val):
        if (node is None):
            node = TreeNode(val)
        elif val<node.data:
            node.left = TreeNode.insert(node.left, val)
        else:
            node.right = TreeNode.insert(node.right, val)
        return node

    def bin_search(node, targetValue):
        if node is None: return False
        testEntry = node.data
        if (targetValue == testEntry):
            return True
        if (targetValue < testEntry):
            return TreeNode.bin_search(node.left, targetValue)
        if (targetValue > testEntry):
            return TreeNode.bin_search(node.right, targetValue)


    def inorder(node):
        if node:
            TreeNode.inorder(node.left)
            print(node.data, end=' ')
            TreeNode.inorder(node.right)
        return

    
    def preorder(node):
        if node:
            print(node.data, end=' ')
            TreeNode.preorder(node.left)
            TreeNode.preorder(node.right)
        return


    def postorder(node):
        if node:
            TreeNode.postorder(node.left)
            TreeNode.postorder(node.right)
            print(node.data, end=' ')
        return
    def depth(node,self):
        if node is None:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(
                node.right))
    def count(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.count(node.left) + self.count(node
                                                          .right)
    
        



root = TreeNode('D')

TreeNode.insert(root, 'A')
TreeNode.insert(root, 'B')
TreeNode.insert(root, 'C')
TreeNode.insert(root, 'E')
TreeNode.insert(root, 'F')
TreeNode.insert(root, 'I')
TreeNode.insert(root, 'J')


TreeNode.postorder(root)