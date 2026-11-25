class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

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

#findmax() , findmin() -remaining


tree = bst()

tree.insert(100)
tree.insert(10)
tree.insert(450)
tree.insert(4)
tree.insert(65)
tree.insert(300)
tree.insert(500)
tree.insert(50)

# print("inorder traversal:")
# tree.inorder(tree.root)

# print("\n\npreorder traversal:")
# tree.preorder(tree.root)

# print("\n\npostorder traversal:")
# tree.postorder(tree.root)

# tree.root = tree.del_node(tree.root, 4)

# print("\n\ninorder after deletion:")
# tree.inorder(tree.root)

# tree.root = tree.del_node(tree.root, 65)

# print("\n\ninorder after deletion:")
# tree.inorder(tree.root)

# tree.root = tree.del_node(tree.root, 100)

# print("\n\ninorder after deletion:")
# tree.inorder(tree.root)

if tree.search(55):
    print("node found")
else:
    print("node not found")