class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None
        self.cnt=0

    def insert(self, data):
        self.root = self.insert_node(self.root, data)

    def insert_node(self, root, data):
        if root is None:
            return node(data)

        if data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        return root

    def del_node(self, rt, val):
        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            # node with only right child or no child
            if rt.left is None:
                return rt.right

            # node with only left child
            if rt.right is None:
                return rt.left

            # node with two children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def cnt_leafNodes(self,rt):
        if rt is None:
            return
        else:
            self.cnt_leafNodes(rt.left)
            if rt.left is None and rt.right is None:
                self.cnt+=1
            self.cnt_leafNodes(rt.right)

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt=0
        level=0
        arr.append(rt)
        while(cnt<len(arr)):
            node_cnt=len(arr)-cnt           #no.of nodes on the current level
            print("level:",level,"=", end=" ")
            for i in range(node_cnt):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ") #visiting node
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1
#findmax() , findmin() -remaining


bst = bst()

bst.insert(100)
bst.insert(10)
bst.insert(450)
bst.insert(4)
bst.insert(65)
bst.insert(300)
bst.insert(500)
bst.insert(50)

# print("inorder traversal:")
# bst.inorder(bst.root)
# print("total leaf nodes:",bst.cnt_leafNodes(bst.root))

# print("\n\npreorder traversal:")
# bst.preorder(bst.root)

# print("\n\npostorder traversal:")
# bst.postorder(bst.root)

# bst.root = bst.del_node(bst.root, 4)

# print("\n\ninorder after deletion:")
# bst.inorder(bst.root)

# bst.root = bst.del_node(bst.root, 65)

# print("\n\ninorder after deletion:")
# bst.inorder(bst.root)

# bst.root = bst.del_node(bst.root, 100)

# print("\n\ninorder after deletion:")
# bst.inorder(bst.root)

# if bst.search(55):
#     print("\nnode found")
# else:
#     print("\nnode not found")

bst.level_order(bst.root)