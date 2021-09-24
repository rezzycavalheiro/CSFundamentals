'''
 Linked lists store references as part of their own elements. 
 Each element of a linked list is called a node, and every node has two different fields:
- data contains the value to be stored in the node;
- next contains a reference to the next node on the list.
'''

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def insert_node_last(self, value):
        new_node = Node(value)
        # Start at the beginning of the list
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def list_size(self):
        curr_node = self.head
        print(self.head)
        print(curr_node)
        total = 0
        while curr_node != None:
            total += 1
            curr_node = curr_node.next

        
    def traverse_list(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
            # nodes.append("None")
        print(" -> ". join(nodes))
        return nodes

linkedList = LinkedList()
a = Node("1")
linkedList.head = a
b = Node("2")
a.next = b
c = Node("3")
b.next = c

linkedList.traverse_list()

d = Node("4")
linkedList.insert_node_first(d)

linkedList.traverse_list()

''' 
Output:
1 -> 2 -> 3
4 -> 1 -> 2 -> 3
'''

f = Node("8")
linked_list = linkedList.traverse_list()
linkedList.insert_node_last(f, linked_list)
