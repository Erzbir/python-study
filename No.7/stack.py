class Stack(object):

    def __init__(self):
        self.__data = []

    def stack_pop(self):
        return self.__data.pop()

    def stack_push(self, item):
        self.__data.append(item)


stack = Stack()
for i in range(5):
    stack.stack_push(i)
for i in range(5):
    print(stack.stack_pop())
