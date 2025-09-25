class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
       self.items.append(item)

    def is_empty(self) -> bool:
        return not self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self) -> int:
        return len(self.items)