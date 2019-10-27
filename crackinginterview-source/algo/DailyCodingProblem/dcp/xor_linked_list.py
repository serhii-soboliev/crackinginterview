class XorNode:
    """
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields,
    it holds a field named both, which is an XOR of the next node and the previous node.
    Implement an XOR linked list;
    it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
    """

    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next


class XorLinkedList:

    POINTER_NOWHERE = -1

    def __init__(self):
        self.mm = MemoryMock()
        self.head_pointer = self.POINTER_NOWHERE
        self.tail_pointer = self.POINTER_NOWHERE

    def add(self, value):
        if self.head_pointer == self.POINTER_NOWHERE:
            n = XorNode(value, self.POINTER_NOWHERE , self.POINTER_NOWHERE)
            n_pointer = self.mm.get_pointer(n)
            self.head_pointer = n_pointer
            self.tail_pointer = n_pointer
        else:
            tail_node = self.mm.dereference_pointer(self.tail_pointer)
            new_tail_node = XorNode(value, self.tail_pointer, self.POINTER_NOWHERE)
            self.tail_pointer = self.mm.get_pointer(new_tail_node)
            tail_node.both = tail_node.both ^ self.POINTER_NOWHERE ^ self.tail_pointer

    def get(self, index):
        current_idx = 0
        current_pointer = self.head_pointer
        current_node = self.mm.dereference_pointer(current_pointer)
        previous_pointer = self.POINTER_NOWHERE
        while current_idx < index:
            next_pointer = current_node.both ^ previous_pointer
            next_node = self.mm.dereference_pointer(next_pointer)
            previous_pointer = current_pointer
            current_pointer = next_pointer
            current_node = next_node
            current_idx += 1
        return current_node

    def size(self):
        current_size = 0
        current_pointer = self.head_pointer
        previous_pointer = self.POINTER_NOWHERE
        while current_pointer != self.POINTER_NOWHERE:
            current_node = self.mm.dereference_pointer(current_pointer)
            next_pointer = current_node.both ^ previous_pointer
            previous_pointer = current_pointer
            current_pointer = next_pointer
            current_size += 1
        return current_size


class MemoryMock:

    def __init__(self):
        self.memory = []

    def get_pointer(self, obj_in_memory):
        self.memory.append(obj_in_memory)
        return self.memory.index(obj_in_memory)

    def dereference_pointer(self, pointer):
        return self.memory[pointer]