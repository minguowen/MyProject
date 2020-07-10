#coding=utf-8

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()


    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:            #如果树是空的，则对根节点赋值
            self.root = node
        else:                     
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:                      #对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)


    def invertTree(self, root):
        if root:
            invert = self.invertTree
            root.lchild, root.rchild = invert(root.rchild), invert(root.lchild)
            return root


if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for elem in elems:                  
        tree.add(elem)           #逐个添加树的节点		
		
    print('翻转树:')
    root = tree.invertTree(tree.root)
    myQueue = []
    myQueue.append(root)
    print(root.rchild.lchild.rchild.elem)
    if root:
        root = myQueue.pop(0)
        print(root.elem)
        if root.lchild:
            myQueue.append(root.lchild)
            print(list(myQueue))
        if root.rchild:
            myQueue.append(root.rchild)
        
		


