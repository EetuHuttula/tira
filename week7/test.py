class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node, depth):
        count = 0
        depth = 1
        if len(node.children) == 2:
                count += 1
        for child in node.children:
            count += find_levels(child, depth - 1)
        return count

if __name__ == "__main__":
            import random, time
        # 1️⃣ Yksi solmu — ei lapsia
t1 = Node("A")
print("T1:", find_levels(t1, 0))  # odotettu 0

# 2️⃣ Yksi lapsi
t2 = Node("A", [Node("B")])
print("T2:", find_levels(t2, 1))  # odotettu 0

# 3️⃣ Ketju (A -> B -> C -> D)
t3 = Node("A", [Node("B", [Node("C", [Node("D")])])])
print("T3:", find_levels(t3, 5))  # odotettu 0

# 4️⃣ Sekoitettu: joillakin lapsia, mutta aina vain 1
t4 = Node("A", [
    Node("B", [Node("C")]),
    Node("D")  # A:lla on 2 lasta, joten tämä ON laskettava
])
print("T4:", find_levels(t4, 1))  # odotettu 1, koska A:lla 2 lasta

# 5️⃣ Syvempi mutta aina vain 1 lapsi
t5 = Node("A", [Node("B", [Node("C", [Node("D", [Node("E")])])])])
print("T5:", find_levels(t5, 2))  # odotettu 0

# 6️⃣ Satunnainen, mutta rajoitetaan lapsimäärä max 1
import random

def random_chain(depth=0, max_depth=8):
    """ Luo satunnainen puu, jossa jokaisella solmulla enintään 1 lapsi """
    if depth >= max_depth or random.random() < 0.3:
        return Node(random.randint(1, 9))
    return Node(random.randint(1, 9), [random_chain(depth+1, max_depth)])

t6 = random_chain()
print("T6:", t6)
print("→ find_levels =", find_levels(t6, 6))  # pitäisi olla aina 0
