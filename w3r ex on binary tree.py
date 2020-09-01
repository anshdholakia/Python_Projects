# Write a Python program to create a Balanced Binary Search Tree (BST)
# using an array (given) elements where array elements are sorted in ascending order
# class Node(object):
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None
#
# def create_link(nums):
#     if len(nums)==0:
#         return None
#     m=len(nums)//2
#     node=Node(nums[m])
#     node.left=create_link(nums[:m])
#     node.right=create_link(nums[m+1:])
#     return node
#
# def preOrder(node):
#     if not node:
#         return
#     print(node.val)
#     preOrder(node.left)
#     preOrder(node.right)
# result = create_link([1, 2, 3, 4, 5, 6, 7])
# preOrder(result)



# Write a Python program to find the closest value of a given target value
# in a given non-empty Binary Search Tree (BST) of unique values
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def closest_value(root, target):
#     a = root.val
#     kid = root.left if target < a else root.right
#     if not kid:
#         return a
#     b = closest_value(kid, target)
#     return min((a, b), key=lambda x: abs(target - x))
#
#
# root = TreeNode(8)
# root.left = TreeNode(5)
# root.right = TreeNode(14)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(8)
# root.left.right.right = TreeNode(7)
# root.right.right = TreeNode(24)
# root.right.right.left = TreeNode(22)
#
# result = closest_value(root, 19)
# print(result)



# Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# def is_BST(root):
#     stack = []
#     prev = None
#
#     while root or stack:
#         while root:
#             stack.append(root)
#             root = root.left
#         root = stack.pop()
#         if prev and root.val <= prev.val:
#             return False
#         prev = root
#         root = root.right
#     return True
#
#
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
#
# result = is_BST(root)
# print(result)
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
#
# result = is_BST(root)
# print(result)



# Write a Python program to delete a node with the given key in a given Binary search tree (BST)
# Definition: Binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def delete_Node(root, key):
#     # if root doesn't exist, just return it
#     if not root:
#         return root
#     # Find the node in the left subtree	if key value is less than root value
#     if root.val > key:
#         root.left = delete_Node(root.left, key)
#     # Find the node in right subtree if key value is greater than root value,
#     elif root.val < key:
#         root.right = delete_Node(root.right, key)
#     # Delete the node if root.value == key
#     else:
#         # If there is no right children delete the node and new root would be root.left
#         if not root.right:
#             return root.left
#         # If there is no left children delete the node and new root would be root.right
#         if not root.left:
#             return root.right
#         # If both left and right children exist in the node replace its value with
#         # the minmimum value in the right subtree. Now delete that minimum node
#         # in the right subtree
#         temp_val = root.right
#         mini_val = temp_val.val
#         while temp_val.left:
#             temp_val = temp_val.left
#             mini_val = temp_val.val
#         # Delete the minimum node in right subtree
#         root.right = deleteNode(root.right, root.val)
#     return root
#
#
# def preOrder(node):
#     if not node:
#         return
#     print(node.val)
#     preOrder(node.left)
#     preOrder(node.right)
#
#
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(7)
# print("Original node:")
# print(preOrder(root))
# result = delete_Node(root, 4)
# print("After deleting specified node:")
# print(preOrder(result))



# Write a Python program to convert a given array elements to a height balanced Binary Search Tree (BST)
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def array_to_bst(array_nums):
#     if not array_nums:
#         return None
#     mid_num = len(array_nums)//2
#     node = TreeNode(array_nums[mid_num])
#     node.left = array_to_bst(array_nums[:mid_num])
#     node.right = array_to_bst(array_nums[mid_num+1:])
#     return node
#
# def preOrder(node):
#     if not node:
#         return
#     print(node.val)
#     preOrder(node.left)
#     preOrder(node.right)
#
# array_nums = [1,2,3,4,5,6,7]
#
# print("Original array:")
# print(array_nums)
# result = array_to_bst(array_nums)
# print("\nArray to a height balanced BST:")
# print(preOrder(result))


# Write a Python program to find the kth smallest element in a given a binary search tree.
# class Node(object):
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None
# def kth_smallest(root, k):
#     stack = []
#     while root or stack:
#         while root:
#             stack.append(root)
#             root = root.left
#         root = stack.pop()
#         k -= 1
#         if k == 0:
#             break
#         root = root.right
#     return root.val
#
# root = Node(8)
# root.left = Node(5)
# root.right = Node(14)
# root.left.left = Node(4)
# root.left.right = Node(6)
# root.left.right.left = Node(8)
# root.left.right.right = Node(7)
# root.right.right = Node(24)
# root.right.right.left = Node(22)
#
# print(kth_smallest(root, 2))
# print(kth_smallest(root, 3))
