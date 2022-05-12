''''
@Time:2022/5/11 12:16       
@Author:OliverCHen
@Project: Algorithm   
@Description: 序列化和反序列化二叉搜索树

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。
示例 1：

输入：root = [2,1,3]
输出：[2,1,3]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/serialize-and-deserialize-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        def postOrder(root: TreeNode):
            if root is None:
                return root
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))
        def construct(lower: int,hight: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > hight:
                return None
            var = arr.pop()
            root = TreeNode(var)
            root.right = construct(var, hight)
            root.left = construct(lower, var)
            return root
        return construct(-inf, inf)

