"""
@Author: 邓润庭
@Time:   2021/4/5 22:05
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ret = ""
        def traverse(node):

            if node is None:
                self.ret += ",#"
                return
            self.ret += ","+str(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.ret[1:]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")

        def decode(d):
            if not d:
                return None
            r = d.pop(0)
            if r == "#":
                return None

            ro = TreeNode(int(r))

            ro.left = decode(d)
            ro.right = decode(d)
            return ro

        res = decode(data)

        return res