class Empty(Exception):
    pass

class ArrayStack:
    # LIFO stack implementation using a Python list as underlying storage
    def __init__(self):
        # Create an empty stack
        #why initialize? so that your object has a place to store the data
        self._data = []

    def __len__(self):
        # Return the number of elements in the stack
        return len(self._data)

    def is_empty(self):
        # Return True if the stack is empty
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack
        self._data.append(e)

    def top(self):
        # Return (but do not remove) the top element
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        # Remove and return the top element
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


s = ArrayStack()
s.push(10)
s.push(20)
print(s.top())
print(s.pop())
print(s.is_empty())
print(len(s))