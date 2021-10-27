# * Section 2 (Trees)
#change
import unittest

# * dd: NumTree Data Definition

# A binary tree is either
# Empty; or
# A node containing some value, a left subtree, and a right subtree

class TreeNode:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

	def __eq__(self,other):
		if isinstance(other, TreeNode):
			return self.value == other.value and self.left == other.left and self.right == other.right
		else:
			return False
	 

x = TreeNode(4, TreeNode(9,TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")),TreeNode(42, "mt", TreeNode(7, "mt", "mt")))
y = TreeNode(10, TreeNode(2,'mt', TreeNode(3, 'mt', "mt")),TreeNode(2, "mt", TreeNode(6, "mt", "mt")))
z = TreeNode(20, TreeNode(2,TreeNode(6,'mt','mt'),'mt'), TreeNode(3,'mt',TreeNode(9, 'mt', 'mt')))
j = TreeNode(10, TreeNode(20, 'mt',TreeNode(60,'mt','mt')),'mt')
# * 1:

# A size is
# A number
# binarytree -> number
# Takes a binary tree and returns the number of values in the tree
# def size(btree):
# self.assertEqual(size(x),7)
# self.assertEqual(size(y),5)

def size(bTree):
	if bTree == 'mt':
		return 0
	else:
		return 1 + size(bTree.left) + size(bTree.right)

# * 2:

# A num_leaves is
# A number
# binarytree -> number
# Takes a binary tree and returns the number of nodes that have both empty subtrees
# def num_leaves(bTree):
# self.assertEqual(num_leaves(x),3)
# self.assertEqual(num_leaves(y),2)

def num_leaves(bTree):
	if bTree == 'mt':
		return 0
	if bTree.left == 'mt' and bTree.right == 'mt':
		return 1
	else:
		return num_leaves(bTree.left) + num_leaves(bTree.right)

# * 3:

# A sum is
# A number
# binarytree -> number
# Takes a binary tree and returns the total value of all the numbers
# def sum(bTree, count=0)
# self.assertEqual(sum(x),186)
# self.assertEqual(sum(y),74)

def sum(bTree):
	if bTree == 'mt':
		return 0
	else:
		return bTree.value + sum(bTree.left) +sum(bTree.right)

# * 4:

# skipped

# * 5:

# A has_triple
# Either True; or
# False
# binarytree -> boolean
# Takes a binary tree and checks for a node of value n, and returns true if its immediate child node is 3n
# def has_triple(bTree, n):
# self.assertEqual(has_triple(x), False)
# self.assertEqual(has_triple(y), True)

def has_triple(bTree):
	if bTree == 'mt':
		return False
	if bTree.left != 'mt':
		if 3 * bTree.value == bTree.left.value:
			return True
	if bTree.right != 'mt':
		if 3 * bTree.value == bTree.right.value:
			return True
	return has_triple(bTree.left) or has_triple(bTree.right)

# * 6:

# A sub_one_map is
# A bindary tree
# binarytree -> binarytree
# Takes a binarytree and returns a new binarytree with all values lowered by one
# def sub_one_map(bTree):
# self.assertEqual(sub_one_map(x), TreeNode(3, TreeNode(8,TreeNode(18, "mt", "mt"), TreeNode(1, TreeNode(102, "mt", "mt"), "mt")),TreeNode(41, "mt", TreeNode(6, "mt", "mt")))
# self.assertEqual(sub_one_map(y), TreeNode(9, TreeNode(1,'mt', TreeNode(2, 'mt', "mt")),TreeNode(1, "mt", TreeNode(5, "mt", "mt"))))

def sub_one_map(bTree):
	if bTree == 'mt':
		return 'mt'
	else:
		return TreeNode(bTree.value-1,sub_one_map(bTree.left),sub_one_map(bTree.right))

# * Tests : the test case class for the tree functions

class TestCase(unittest.TestCase):
	def test_size_1(self):
		self.assertEqual(size(x),7)
	def test_size_2(self):
		self.assertEqual(size(y),5)

	def test_num_leaves_1(self):
		self.assertEqual(num_leaves(x),3)
	def test_num_leaves_2(self):
		self.assertEqual(num_leaves(y),2)


	def test_sum_1(self):
		self.assertEqual(sum(x),186)
	def test_sum_2(self):
		self.assertEqual(sum(y),23)

	def test_has_triple_1(self):
		self.assertFalse(has_triple(x))
	def test_has_triple_2(self):
		self.assertTrue(has_triple(y))
	def test_has_triple_3(self):
		self.assertTrue(has_triple(z))
	def test_has_triple_4(self):
		self.assertTrue(has_triple(j))

	def test_sub_one_map_1(self):
		self.assertEqual(sub_one_map(x), TreeNode(3, TreeNode(8,TreeNode(18, "mt", "mt"), TreeNode(1, TreeNode(102, "mt", "mt"), "mt")),TreeNode(41, "mt", TreeNode(6, "mt", "mt"))))
	def test_sub_one_map_2(self):
		self.assertEqual(sub_one_map(y), TreeNode(9, TreeNode(1,'mt', TreeNode(2, 'mt', "mt")),TreeNode(1, "mt", TreeNode(5, "mt", "mt"))))

if __name__ == '__main__':
	unittest.main()
