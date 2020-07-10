# coding=utf-8

class Node(object):
    """节点类"""

    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()

    def add(self, val):
        """为树添加节点"""
        node = Node(val)
        if self.root.val == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:  # 对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if treeNode.left == None:
                    treeNode.left = node
                    return
                elif treeNode.right == None:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == '__main__':
    """主函数"""
    elem = range(10)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for val in elem:
        tree.add(val)  # 逐个添加树的节点

    print('路径求和:')
    flag = tree.hasPathSum(tree.root, 12)
    print(flag)





