# 二叉树最小深度

# from pprint import pprint as print


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def min_depth(root: TreeNode):
    if root is None:
        return 0

    # 初始深度为1
    depth = 1
    q = [root]
    while q:
        size = len(q)
        for _ in range(size):
            node = q.pop(0)
            # 如果是叶子节点，直接返回结果
            if node.left is None and node.right is None:
                return depth
            # 添加下一层节点
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        # 遍历完一层之后，最小深度加1
        depth += 1
    return depth


def build_tree():
    a_node = TreeNode("A")
    b_node = TreeNode("B")
    c_node = TreeNode("C")
    d_node = TreeNode("D")
    e_node = TreeNode("E")
    f_node = TreeNode("F")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.right = f_node
    return a_node


print(min_depth(build_tree()))
