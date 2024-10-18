class Queue(object):
    def __init__(self, size):
        self.size = size

        self.isFull = False
        self.isEmpty = True

        
        self.hp =0
        self.tp = 0
        self.list = [None]*size

    def enq(self, item):
        if (self.isFull):
            print("Queue is full")
            return

        self.list[self.tp] = item
        self.tp = (self.tp + 1) % self.size

        self.isEmpty = False
        if (self.tp == self.hp):
            self.isFull = True

    def deq(self):
        if (self.isEmpty):
            print("Queue is empty")
            return None

        result = self.list[self.hp]
        self.hp = (self.hp + 1) % self.size

        self.isFull = False
        if (self.tp == self.hp):
            self.isEmpty = True
            return result
    
    def dequeueCount(self,node):
        if (self.isEmpty):
            return 0
        count = 0
        temp = node
        while(temp is not None):
            temp = temp.next
            count += 1
            return count
    def stack_inorder(self,node):
        if (self.isEmpty):
            return 0
        count = 0
        temp = node
        while(temp is not None):
            temp = temp.next
            count += 1
            return count
        
        
       