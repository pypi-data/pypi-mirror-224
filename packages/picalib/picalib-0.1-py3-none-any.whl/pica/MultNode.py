class MultNode:
    def __init__(self, node1, node2: int):
        self.value = node1.result
        self.value2 = node2.result
        self.result = self.value * self.value2
        self.gradient = 0
        self.gradient1 = node2
        self.gradient2 = node1
        self.children = [node1,node2]

   