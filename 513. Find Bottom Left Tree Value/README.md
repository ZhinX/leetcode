# 513. Find Bottom Left Tree Value

找出一个二叉树最低左的元素值：

一般涉及到二叉树的深度问题，可以考虑使用BFS从root开始搜索。在本题中，问题变为BFS中最后一轮找最左边的元素，因此在进队时可以先右子树后左子树，这样保证最后进队的元素一定是最左边的元素

---
在实现过程中，一种pythonic的方式是使用filter函数```filter(function, sequence)```,从sequence中找出满足function（一般写lambda函数）的子序列，默认None为```identity()```，即选出不假的元素

在本题中，筛选空子树可以写成```filter(None, [node.right, node.left])```，这样就不用写繁琐的判断条件