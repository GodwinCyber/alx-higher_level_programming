#!/usr/bin/python3

class Node:
    """class that define a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize a node with data and nex_node"""
        self.data = data
        self.next_node = next_node
    
    
    @property
    def data(self):
        """"return the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data of th node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
        
    @property
    def next_node(self):
        """return the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the nex_nod of the nod"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """class that define a singly linked list"""

    def __init__(self):
        """initiate a singly linked list with a header attribute"""
        self.head = None

    def __str__(self):
        """return a string representing a single linked list"""
        s = ""
        node = self.head
        while node:
            s += str(node.data)
            node = node.next_node
            if node:
                s += "\n"
        return s

    def sorted_insert(self, value):
        """insert a new node into correct sorted of the list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            prev = None
            while node and value > node.data:
                prev = node
                node = node.next_node
            if prev is None:
                new_node.next_node = self.head
                self.head = new_node
            else:
                new_node.next_node = node
                prev.next_node = new_node
