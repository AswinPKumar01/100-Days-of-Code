class Solution:
    def recoverTree(self, root: TreeNode) -> None:
       
        nodes = []
        values = []
        self.inorder(root, nodes, values)
        values.sort()
        for i in range(len(nodes)):
            nodes[i].val = values[i]
        
    def inorder(self, root, nodes, values):
        if root:
            self.inorder(root.left, nodes, values)
            nodes.append(root)
            values.append(root.val)
            self.inorder(root.right, nodes, values)
