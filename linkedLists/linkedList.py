
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    

class LinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    def Printing(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next    

    def append(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
            self.length=1  
        else:
            node=Node(value)
            self.tail.next=node
            self.tail=node
            self.length+=1  
        return True    

    def pop(self):
        if(self.length==0):
            return None
        temp=self.head
        prev=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
        self.tail=prev
        self.tail.next=None
        self.length-=1

        if(self.length==0):
            self.head=None
            self.tail=None                

    def prepend(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
        else:
            temp=self.head   
            self.head.next= temp  
            self.head=node
        self.length+=1  
        return True  


    
    def prepop(self):
        if(self.length==0):
            return None 
        temp=self.head
        self.head=self.head.next
        temp.next=None 
        self.length-=1
        if(self.length==0):
            self.tail=None 
        return temp  

    def get_node(self,index):
        temp = self.head
        if(index <0 or index>=self.length):
            return None
        for i in range(index):
            temp = temp.next
        return temp.value

    def set_value(self,index, value):
        node=self.get_node(index)
        if(node):
            node.value = value
            return True
        else:
            False        
    def insert_node(self,index,value):
        node=Node(value)
        if(index <0 or index > self.length):
            return False
        if(index==0):
            return self.prepend(node)
        if(index==self.length):
           return self.append(node)
            

        pre=self.get(index-1)
        node.next=pre.next
        pre.next=node
        self.length+=1
        return True

    def remove_node(self,index):
        if(index <0 or index >= self.length):
            return None

        if(index==0):
            return self.prepop()  
        if(index==self.length-1):
            return self.pop()    

        pre=self.get(index-1)  
        remove=pre.next
        pre.next=remove.next
        remove.next=None
        self.length-=1

        return remove
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None

        for i in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after


        





                

my_LinkedList=LinkedList(5)
my_LinkedList.append(6)
my_LinkedList.pop()
my_LinkedList.Printing()