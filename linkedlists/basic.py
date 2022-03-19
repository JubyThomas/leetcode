class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class LinkedList:
    def __init__(self,head=None):        
        self.head=head
        
    def insert_at_beginning(self,newNode):
        newNode.next=self.head
        self.head=newNode
    
    def insert_at_end(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            #print(current)
            while(current.next!=None):
                current=current.next
            current.next=newNode
    
    def addAtIndex(self, index: int, newNode):
        currentnode=self.head
        if index == 0:
          self.insert_at_beginning(newNode)
        count=0
        while count<index-1: 
             currentnode=currentnode.next
             count+=1
        newNode.next=currentnode.next
        currentnode.next=newNode
        
        # count=1
        # curr=self.head
        # while count<index-1 and curr!=None:
        #     curr=curr.next
        #     count+=1

        # newNode.next=curr.next
        # curr.next=newNode
    
    def get(self,index):
        if index == 0:
            return self.head.val
        else:
            current = self.head
            count = 0
            while current != None:
                if index == count:
                    return current.val
                count += 1
                current = current.next
            return -1
                   
    def display(self):           
        temp = self.head
        while(temp):
            print(temp.val,end=" ")
            temp = temp.next
    
#---------end of singly linked list---------------    
                    
#---call method----  

linkd=LinkedList()
                  
n1=Node(40)
linkd.insert_at_end(n1)

n2=Node(90)
linkd.insert_at_end(n2)

n3=Node(190)
linkd.insert_at_end(n3)

n4=Node(290)
linkd.insert_at_end(n4)


n4=Node(87)
linkd.insert_at_beginning(n4)


linkd.display()
print("\n")
n5=Node(13)
linkd.addAtIndex(2,n5)

print(linkd.get(2))

linkd.display()
            
                 
        
    