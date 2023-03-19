# general tree
class GenericTreeNode:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = " "*level+str(self.data) + "\n"

        for child in self.children:
            ret += child.__str__(level+1)

        return ret

    def addChild(self, GenericTreeNode):
        self.children.append(GenericTreeNode)


tree = GenericTreeNode("Drinks", [])
cold = GenericTreeNode('cold', [])
hot = GenericTreeNode('hot', [])
tea = GenericTreeNode('tea', [])
coffee = GenericTreeNode('coffee', [])
cola = GenericTreeNode('cola', [])
fanta = GenericTreeNode('fanta', [])
tree.addChild(cold)
tree.addChild(hot)
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)
