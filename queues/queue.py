class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class Queue:
    def __init__(self,value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length=1

    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next    

    def enQueue(self,value):
        node = Node(value)
        if(self.length==0):
            self.first=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
        self.length+=1 
        return True

    def deQueue(self):
        if(self.first is None):
            return None
        temp=self.first
        if(self.length==1):
            self.first=None
            self.last=None   
        else:
            self.first=temp.next
            temp.next =None
        self.length-=1
        return temp         

queue=Queue(2)

queue.print_queue()

