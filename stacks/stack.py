class Node:
    def __init__(self,value):
        self.value = value
        self.next=None


class Stack:
    def __init__(self,value):
        node = Node(value)
        self.top=node
        self.height=1

    def print_node(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def push(self,value):
        node=Node(value)
        if(self.height==0):
            self.top=node
            self.height=1
        else:
            node.next=self.top
            self.top=node
        self.height+=1
        return True


    def pop(self):
        if(self.height==0):
            return None
        temp=self.top
        self.top=temp.next
        temp.next=None
        self.height-=1
        return temp


stacker=Stack(1)
stacker.push(6)
stacker.pop()
stacker.print_node()        

