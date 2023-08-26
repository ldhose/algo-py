
def linked_list_test():
    list = LinkedList()
    list.add_first(Node("9"))
    list.add_last(Node("10"))
    print(list)
    list.add_after("10", Node("11"))
    print(list)
    list.add_before("9", Node("7"))
    print(list)
    list.add_before("9", Node("8"))
    print(list)
    list.remove_node("7")
    list.remove_node("9")
    print(list)

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = [] 
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, after_element, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == after_element:
                new_node.next = node.next
                node.next = new_node
                return

    def add_before(self, target_element, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_element:
            self.add_first(new_node)
            return
        prev_node = self.head
        for node in self:
            if node.data == target_element:
                new_node.next = prev_node.next
                prev_node.next = new_node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_element)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("No matching node to remove")


    
                

                




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data    