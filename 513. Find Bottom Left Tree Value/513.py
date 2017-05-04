# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        node = TreeNode(-1)
        while len(queue):
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

        # elegant method
        # queue = [root]
        # for node in queue:
        #     queue += filter(None, [node.right, node.left])
        # return queue[-1].val