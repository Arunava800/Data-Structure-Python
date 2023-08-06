import random


class Node:
    def __init__(self, key, level):
        self.key = key
        # list to hold references to node of different levels
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_lvl, p):
        # Maximum level skip list
        self.MAX_LVL = max_lvl
        # P is the fraction of the nodes with level
        # I references also having level i+1 references
        self.P = p
        # Create header node and initialize key to -1
        self.header = self.create_node(self.MAX_LVL, -1)
        # current level of skip list
        self.level = 0

    def create_node(self, lvl, key):
        n = Node(key, lvl)
        return n

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LVL:
            lvl += 1
            return lvl

    def insert_element(self, key):
        update = [None] * (self.MAX_LVL + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            r_level = self.random_level()
            if r_level > self.level:
                for i in range(self.level + 1, r_level + 1):
                    update[i] = self.header
                self.level = r_level

            n = self.create_node(r_level, key)

            for i in range(r_level+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("Key {} inserted successfully".format(key))



lst = SkipList(3, 0.5)
lst.insert_element(6)
