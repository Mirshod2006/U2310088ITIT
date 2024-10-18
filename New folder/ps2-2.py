class TreeNode:
    def init(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    result = []
    current_level = [root]

    while current_level:
        next_level = []
        current_values = []

        for node in current_level:
            current_values.append(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(current_values)
        current_level = next_level

    return result