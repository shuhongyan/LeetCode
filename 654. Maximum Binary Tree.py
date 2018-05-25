#392ms
#时间好长我的天
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        tree = TreeNode(None)
        if nums == []:
            return None
        tree.val = max(nums)
        i = nums.index(max(nums))
        tree.left = self.constructMaximumBinaryTree(nums[:i])
        tree.right = self.constructMaximumBinaryTree(nums[i+1:])
        return tree
#172ms
#感觉逻辑是一样的啊，但是runtime咋差这么多呢
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        tree=TreeNode(None)
        def m(tree, nums):
            
            i = nums.index(max(nums))
            tree.val = nums[i]
            if nums[:i]:
                tree.left = TreeNode(None)
                m(tree.left,nums[:i])
            if nums[i+1:]:
                tree.right = TreeNode(None)
                m(tree.right, nums[i+1:])
                
        m(tree, nums)
        return tree
        