class TreeNode:
    def init(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.value != q.value:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)