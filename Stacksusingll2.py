#creating a blueprint
class StackBox:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_box = StackBox(value)
        new_box.next = self.top
        self.top = new_box

    def pop(self):
        if self.top is None:
            print("Stack is empty!")
            return
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            print("Stack is empty!")
            return
        return self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Top:", stack.peek())  # Top: 30
print("Popped:", stack.pop())  # Popped: 30
stack.display()
