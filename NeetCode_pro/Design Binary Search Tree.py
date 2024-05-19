from typing import List


class TreeNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)

        # se a BST está vazia
        # adiciona o novo nó como root
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            # a key a inserir tem de ir para esquerda
            if key < current.key:
                # quando nao tiver nada à esquerda, adicionar ai
                if not current.left:
                    current.left = new_node
                    return
                # ainda existem nodes À esquerda
                current = current.left
            # a key a inserir tem de ir para direita
            elif key > current.key:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            # a key ja existe, vamos substituir o valor
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root

        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        min = self.find_min_node(self.root)
        return min.val if min else -1

    def getMax(self) -> int:
        max = self.find_max_node(self.root)
        return max.val if max else -1

    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorder(self.root, res)
        return res

    def find_min_node(self, node):
        current = node
        while current and current.left:
            current = current.left

        return current

    def find_max_node(self, node):
        current = node
        while current and current.right:
            current = current.right

        return current

    def inorder(self, node, res):
        if not node:
            return

        self.inorder(node.left, res)
        res.append(node.key)
        self.inorder(node.right, res)

    def remove_helper(self, root: TreeNode, key):
        if not root:
            return None

        if key > root.key:
            root.right = self.remove_helper(root.right, key)
        elif key < root.key:
            root.left = self.remove_helper(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.find_min_node(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.remove_helper(root.right, min_node.key)

        return root
