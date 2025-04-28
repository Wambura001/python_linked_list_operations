'''
SIRINCHA MESHACK WAMBURA
'''

class Node:
    def __init__(self, value = None, next = None):
        self.item = value
        self.link = next

class Linked_list:
    def __init__(self):
        self.head = None

    #  DISPLAY LIST 
    def display_list(self):
        if self.head is None: 
            print("No Element!")
            return 
        else: 
            node = self.head
            while node is not None:
                print(" ", node.item)
                node = node.link

    # INSERTION AT THE HEAD
    def add_first(self, value): 
        new_node = Node(value)
        new_node.link = self.head
        self.head = new_node

    # iNSERTING AT THE TAIL 
    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 
        x = self.head
        while x.link is not None:
            x = x.link
        x.link = new_node
    
    # DELETION AT THE HEAD
    def remove_front(self):
        if self.head is None:
            print("List is empty!")
            return
        self.head = self.head.link 

    # DELETING AT THE TAIL 
    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        x = self.head
        while x.link.link is not None:
            x = x.link
        x.link = None



list1 = Linked_list()
list1.add_first(23)
list1.add_first(53)
list1.add_last(73)
list1.add_last(83)
list1.display_list()