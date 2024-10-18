
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

# singly linked list
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # access element in list, O(n)
    def get(self, i):
        return self.getNode(i).data

    # access element in list, O(n)
    def getNode(self, i):
        if i >= self.size:
            raise Exception('Out of index range')
        el = self.head
        for _ in range(i):
            el = el.next
        return el

    # add element at the head, O(1)
    def prepend(self, item):
        n = Node(item)
        n.next = self.head
        self.head = n
        self.size += 1

    # add element at the end, O(n)
    def append(self, item):
        n = Node(item)

        # list is empty, assign to head
        if self.head is None:
            self.head = n
            return

        # list not empty, traverse till the end
        last = self.head
        while(last.next):
            last = last.next

        last.next = n
        self.size += 1

    # insert new element after node, O(1)
    def insertAfter(self, afterNode, item):
        n = Node(item)
        n.next = afterNode.next
        afterNode.next = n
        self.size += 1

    # find an element, O(n)
    def findIndex(self, item):
        i = 0
        temp = self.head
        while temp:
            if (temp.data == item):
                return i
            temp = temp.next
            i += 1
        return -1

    # remove element from the list, O(n)
    def remove(self, item):
        i = self.findIndex(item)
        if i == 0:
            self.head = self.head.next
            self.size -= 1
        elif i > 0 and i < self.size:
            cur = self.getNode(i)
            prev = self.getNode(i-1)
            prev.next = cur.next
            self.size -= 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def length(self):
        return self.size
    # Testing
    def index(self,node):
        i = 0
        temp = self.head
        while temp:
            temp = temp.next
            i += 1
        return i
    
        



if __name__ == '__main__':

    s = SinglyLinkedList()

    s.prepend(1)
    s.prepend(2)
    s.prepend(3)

    s.append(4)
    s.append(5)


    n = s.getNode(0)

    s.insertAfter(n, 6)

    s.print()