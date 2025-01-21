# singly linked list


class SinglyLinkedList:
    def __init__(self, val, next_val=None):
        self.val = val
        self.next_val = next_val

    def __str__(self):
        return self.val
