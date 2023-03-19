class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None

    def listtraversing(self):
        printvalue = self.head

        while printvalue:
            print(printvalue.data)
            printvalue = printvalue.next

    def insertBegining(self, data=None):
        newNode = Node(data or "Sun")
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data=None):
        newNode = Node(data or "Thu")
        if not self.head:
            self.head.next = newNode
            return
        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

    def insertBetween(self, node, data):
        if not node:
            print("middle node is absent!!")
            return

        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode


list1 = SLinkedList()
list1.head = Node("Mon")
n2 = Node('Tue')
n3 = Node('Wed')

list1.head.next = n2
n2.next = n3
list1.insertBegining()
list1.insertBetween(n2, "wed")
list1.listtraversing()
