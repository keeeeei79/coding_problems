import json
import copy


class Node:
    def __init__(self, key: int, left=None, right=None, parent=None) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def _conv_dict(self, node_dict: dict) -> dict:
        del node_dict["parent"]
        if node_dict["left"]:
            left = node_dict["left"].__dict__.copy()
            left = self._conv_dict(left)
            node_dict["left"] = left
        if node_dict["right"]:
            right = node_dict["right"].__dict__.copy()
            right = self._conv_dict(right)
            node_dict["right"] = right
        return node_dict

    def __str__(self) -> str:
        node = self.__dict__.copy()
        return json.dumps(self._conv_dict(node), indent=2)


class BSTRoot:
    def __init__(self, init_z: int) -> None:
        self.root: Node = Node(init_z)

    def __str__(self) -> str:
        return str(self.root)

    def insert(self, z: int) -> None:
        node = Node(key=z)
        x = self.root
        while x:
            parent = x
            if x.key > node.key:
                x = x.left
            else:
                x = x.right
        node.parent = parent
        if parent.key > node.key:
            parent.left = node
        else:
            parent.right = node

    def find(self, z: int) -> bool:
        x = self.root
        while x:
            if x.key == z:
                return True
            elif x.key > z:
                x = x.left
            else:
                x = x.right
        return False

    def delete(self, z: int) -> None:
        # 子Nodeが0の場合はそのまま削除
        # 子Nodeが1の場合は子Nodeをそのまま昇格させる
        # 子Nodeが2の場合は子右部分木のうち最小のものを削除したNodeの位置に持ってくる
        self._delete(self.root, z)

    def _get_successor(self, node: Node) -> Node:
        node = node.right
        while node.left:
            node = node.left
        return copy.deepcopy(node)

    def _delete(self, node: Node, z: int) -> None:
        # root内でkey=zのNodeを削除する
        if z < node.key:
            self._delete(node.left, z)
        elif z > node.key:
            self._delete(node.right, z)
        else:
            if not node.left and not node.right:
                # 子ノードが存在しない場合
                parent = node.parent
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            elif not node.left or not node.right:
                # 子ノードが1つ存在する場合
                parent = node.parent
                child_node = node.left if node.left else node.right
                if parent.left == node:
                    parent.left = child_node
                else:
                    parent.right = child_node
                child_node.parent = parent
            else:
                # 子ノードが2つ存在する場合
                successor = self._get_successor(node)
                successor.parent = node.parent
                successor.left = node.left
                node.left.parent = successor
                successor.right = node.right
                node.right.parent = successor
                # nodeの場所にsuccessorを代入
                if node.parent:
                    parent = node.parent
                    if parent.left == node:
                        parent.left = successor
                    else:
                        parent.right = successor
                else:
                    # 削除するのがrootなら置き換える
                    self.root = successor
                # 元のsuccessorを削除
                self._delete(node.right, successor.key)


root = BSTRoot(10)
root.insert(4)
root.insert(2)
root.insert(11)
root.insert(3)
root.insert(5)
print(root)

print(root.find(4))
print(root.find(0))

root.delete(10)  # メモリリークがありそうな気がするがとりあえずok
print(root)
