class Queue:
    def __init__(self):
        self.__data = []

    def join(self, data):
        self.__data.append(data)

    def out(self):
        return self.__data.pop(0)


queue = Queue()
for i in range(5):
    queue.join(i)
for i in range(5):
    print(queue.out())

