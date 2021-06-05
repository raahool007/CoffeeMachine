class Stack():

    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, el):
        self.arr.append(el)
        self.length += 1

    def pop(self):
        if self.length != 0:
            el = self.arr[self.length - 1]
            self.arr[self.length - 1] = None
            self.length -= 1
            return el
        else:
            return None

    def peek(self):
        return self.arr[self.length - 1]

    def is_empty(self):
        return self.length == 0