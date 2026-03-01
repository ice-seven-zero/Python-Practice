class Node:
    def __init__(self, elem=-1,lchild=None, rchild=None):
        #lchild=None这是默认参数，如果不传参，会使用定义时的默认值。
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.myqueue=[]

    def insert(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
            self.myqueue.append(node)#append是队尾入结点
        else:
            treenode=self.myqueue[0]
            if treenode.lchild is None:
                treenode.lchild=node
                self.myqueue.append(node)
            elif treenode.rchild is None:
                treenode.rchild=node
                self.myqueue.append(node)
                self.myqueue.pop(0)#该结点的左右子树都配完之后要把该节点从队列中弹出去

#前序遍历二叉树
def PreOrder(node:Node):
    #node:Node这个意思是写注释，作用是方便联想
    if node:
        print(node.elem,end=' ')
        PreOrder(node.lchild)
        PreOrder(node.rchild)

#层次遍历二叉树
def LeverOrder(root:Node):
    if root is None:
        return
    queue1=[]
    queue1.append(root)
    while queue1:#层次遍历用while循环，并不用递归
        node=queue1.pop(0)
        print(node.elem,end=' ')
        if node.lchild:
            queue1.append(node.lchild)
        if node.rchild:
            queue1.append(node.rchild)



if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        tree.insert(i)

    #PreOrder(tree.root)
    LeverOrder(tree.root)