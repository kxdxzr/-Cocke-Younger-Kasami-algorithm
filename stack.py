class Stack:
    def __init__(self):
        self.memory = []

    def pop(self):
        self.memory.pop(0)

    def push(self, new_variable):
        self.memory.insert(0,new_variable)

    def show_current(self):
        return self.memory[0]

    def show_length(self):
        return len(self.memory)
