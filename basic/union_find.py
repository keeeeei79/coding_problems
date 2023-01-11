from collections import defaultdict


class UnionFind:
    def __init__(self) -> None:
        self.parent_dic: dict = defaultdict(lambda: -1)
        self.size_dic: dict = defaultdict(lambda: 1)

    def root(self, x: int) -> int:
        if self.parent_dic[x] == -1:
            return x
        else:
            root = self.root(self.parent_dic[x])
            self.parent_dic[x] = root  # 経路圧縮
            return root

    def size(self, x: int) -> int:
        return self.size_dic[self.root(x)]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> None:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return

        # union by size
        if self.size_dic[x] < self.size_dic[y]:
            x, y = y, x

        self.parent_dic[y] = x
        self.size_dic[x] += self.size_dic[y]


uf = UnionFind()
uf.unite(1, 2)
uf.unite(2, 3)
uf.unite(5, 6)
print(uf.is_same(1, 3))
print(uf.is_same(2, 5))
