class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __show__(self):
        cur = self
        while cur:
            print(cur.value, end=" -> " if cur.next != None else "\n")
            cur = cur.next

    

def reverseLinkedList(head):
    # Create two pointers
    prevNode, nextNode = None, None

    # While we are still following the linked list
    while head:
        # Move next up by one
        # Here, all three pointers are pointing to their respective names
        nextNode = head.next
        # Reverse the direction of the upcoming link
        head.next = prevNode
        # Move prev and current up by one
        prevNode = head
        head = nextNode
    return prevNode

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)
node1.__show__()
reverseLinkedList(node1)
node3.__show__()

class GraphNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __show__ (self) :
        if self.left:
           self.left.__show__()
        print (self.data, end=" ")
        if self.right:
           self.right.__show__()


def invertTree(root):
    if root == None:
        return
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

node3 = GraphNode(3)
node2 = GraphNode(2)
node1 = GraphNode(1)
node1.left, node1.right = node2, node3
node1.__show__()
invertTree(node1)
node1.__show__()