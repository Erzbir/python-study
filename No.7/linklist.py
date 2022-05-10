class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

    def getData(self):
        return self.item

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def setData(self, item):
        self.item = item


class LinkList:

    def __init__(self):
        self.__head = None

    def isempty(self):
        return self.__head is None

    def length(self):
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        node = Node(item)
        if self.isempty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        if index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def printf(self):
        cur = self.__head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def remove(self, item):
        cur = self.__head
        found = False
        pre = None
        while not found:
            if cur.item == item:
                found = True
            else:
                pre = cur
                cur = cur.next
        if pre is None:
            self.__head = cur.next
        else:
            pre.next = cur.next


L = LinkList()
for a in range(3):
    L.append(a)
L.insert(1, 99)
for a in L.printf():
    print(a)
L.remove(2)
print()
for a in L.printf():
    print(a)
