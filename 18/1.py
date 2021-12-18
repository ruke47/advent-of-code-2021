import math
from typing import Optional, Union, Iterator

verbose = 0

class Node:
    def __init__(self, left, right, parent: Optional['Node'] = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0

    def try_explode(self) -> bool:
        if isinstance(self.left, Node):
            if self.left.try_explode():
                return True
        if self.depth >= 4:
            self.explode()
            return True
        if isinstance(self.right, Node):
            return self.right.try_explode()
        else:
            return False

    def explode(self):
        if not isinstance(self.left, int) or not isinstance(self.right, int):
            print(f"Trying to explode non-terminal node")
            print(self.get_root())

        if verbose > 1:
            print("\tExplode:")
            print(f"\t{self.get_root()}")
            print("\t-->")

        self.add_left(self.left)
        self.add_right(self.right)
        if self == self.parent.left:
            self.parent.left = 0
        else:
            self.parent.right = 0

        if verbose > 1:
            print(f"\t{self.get_root()}")

    def add_left(self, value):
        current = self
        while True:
            if not current.parent:
                return
            if current == current.parent.left:
                current = current.parent
            else:
                current = current.parent
                break
        if isinstance(current.left, int):
            current.left += value
        else:
            current = current.left
            while isinstance(current.right, Node):
                current = current.right
            current.right += value

    def add_right(self, value):
        current = self
        while True:
            if not current.parent:
                return
            if current == current.parent.right:
                current = current.parent
            else:
                current = current.parent
                break
        if isinstance(current.right, int):
            current.right += value
        else:
            current = current.right
            while isinstance(current.left, Node):
                current = current.left
            current.left += value

    
    def try_split(self):
        if isinstance(self.left, Node):
            if self.left.try_split():
                return True
        elif isinstance(self.left, int) and self.left >= 10:
            if verbose > 1:
                print("\tSplit:")
                print(f"\t{self.get_root()}")

            cl = math.floor(self.left / 2)
            cr = math.ceil(self.left / 2)
            self.left = Node(cl, cr, self)

            if verbose > 1:
                print("\t-->")
                print(f"\t{self.get_root()}")

            return True

        if isinstance(self.right, Node):
            return self.right.try_split()
        elif isinstance(self.right, int) and self.right >= 10:
            if verbose > 1:
                print("\tSplit:")
                print(f"\t{self.get_root()}")

            cl = math.floor(self.right / 2)
            cr = math.ceil(self.right / 2)
            self.right = Node(cl, cr, self)

            if verbose > 1:
                print("\t-->")
                print(f"\t{self.get_root()}")

            return True

        return False

    def get_root(self):
        root = self
        while root.parent:
            root = root.parent
        return root

    def discover_parents(self, parent=None):
        if parent:
            self.parent = parent
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        if isinstance(self.left, Node):
            self.left.discover_parents(self)
        if isinstance(self.right, Node):
            self.right.discover_parents(self)

    def magnitude(self):
        lmag = self.left if isinstance(self.left, int) else self.left.magnitude()
        rmag = self.right if isinstance(self.right, int) else self.right.magnitude()
        return 3 * lmag + 2 * rmag

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def __repr__(self):
        return self.__str__()


def parse_fishint(it: Iterator[str]) -> Union[Node, int]:
    c = next(it)
    if c.isdigit():
        return int(c)
    if c == '[':
        left = parse_fishint(it)
        comma = next(it)
        if comma != ',':
            print(f"Parsing error: {comma} is not a comma")
            exit(-1)
        right = parse_fishint(it)
        close = next(it)
        if close != ']':
            print(f"Parsing error: {close} is not a closing brace")
        return Node(left, right)

def add(a: Node, b:Node) -> Node:
    if verbose > 0:
        print("------")
        print(a)
        print("+")
        print(b)
        print("=")
    new_root = Node(a, b)
    new_root.discover_parents()
    if verbose > 0:
        print(new_root)
    while True:
        if new_root.try_explode():
            continue
        if new_root.try_split():
            continue
        break
    if verbose > 0:
        print("-->")
        print(new_root)
        print("")
    return new_root


fishints = []
with open("input.txt") as file:
    for line in file:
        it = iter(line.strip())
        fishint = parse_fishint(it)
        fishint.discover_parents()
        fishints.append(fishint)

cur_fish = fishints[0]
for addfish in fishints[1:]:
    cur_fish = add(cur_fish, addfish)

print(f"Final Magnitude: {cur_fish.magnitude()}")