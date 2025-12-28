class node:
    #create empty node
    def __init__(self,value):
        self.data = value
        self.next = None

    
a = node(1)
print(a.next)
print(a.data)


class linkedlist:
    #creat empty head and count the elements
    def __init__(self):
        #empty linked list
        self.head = None
        self.n =0
    #length function
    def __len__(self):
        return self.n
    #insert data by head
    def inserthead(self,value):
        new_node = node(value)
        new_node.next= self.head
        self.head =new_node
        self.n = self.n+1
    #print the linklist 
    def __str__(self):
        curr = self.head
        result =''
        while curr!=None:
            result = result + str(curr.data)+'->'
            curr = curr.next
        return result[:-2]
    #append function
    def append(self,value):
        new_node = node(value)
        #case 1 empty list agar hai to
        if self.head == None:
            self.head =new_node
            self.n = self.n+1
            return
        #case 2 : non empty list
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            #we are in last node
        #attach last node
        curr.next = new_node
        self.n = self.n+1

    #insert node in middle
    def insert_after(self,after,value):
        #new node created
        new_node = node(value)
        #putting head value inside curr
        curr = self.head
        #making loop so every node will run from the end
        while curr!=None:
            #know compare that curr.data value is equall to after which is over target when find it
            if curr.data == after:
                #know put the address inside the new node
                new_node.next=curr.next
                #and joint both node and walk away
                curr.next = new_node
                self.n+=1
                return
            #if not found move on to next
            curr = curr.next
        return 'item not found'
    #clear the linked list by removing all node references
    def clear(self):
        self.head = None
        self.n = 0
    #we create a delete function to delete the head of a node by simple logic assign the head value to next node
    def delete_head(self):
        #if head is empty return empty ll
        if self.head == None:
            return 'empty linked list'
        self.head = self.head.next
        self.n-=1
    
    #we create a pop function with simple logic the address of secound last node will be none
    def pop(self):
        #first we cheak head is empty or not
        if self.head ==None:
            return 'empty ll'
        # assign head to curr
        curr = self.head
        #if there is only one node then delete it by using delete_head function
        if curr.next == None:
            return self.delete_head()
        #looping until secound last node reaches  
        while curr.next.next!=None:
            #put the value of curr.next in curr
            curr = curr.next
        #it means we are delete the last node and making it empty
        curr.next = None
        self.n -= 1
    #making remove functioin so we can remove any element
    def remove(self,value):
        #if head is none return empty ll
        if self.head == None:
            return 'empty ll'
        #if there is only one head delete it
        if self.head.data == value:
            return self.delete_head()
        #curr assign the head so we can traverse
        curr = self.head
        # making a loop so we can stop secound lastor we can say last element
        while curr.next!=None:
            #if data is == to value means if we get what we are finding in ll then break
            if curr.next.data==value:
                curr.next = curr.next.next
                self.n-=1
                return
            # if dont find go to next node
            curr = curr.next
        #if nodes is empty return not found
        return 'not found'
    #we are making searching a element in node
    def search(self,item):
        #we assign value to curr so we can traverse and make a empty variable
        curr =self.head
        pos=0
        #loop work until the last node
        while curr!=None:
            #id data is matches the item return the pos or else continue 
            if curr.data == item:
                return pos
            curr = curr.next
            pos+=1
        return 'not found'
    #making a function so we can find any element by its nodes
    def __getitem__(self,index):
        #givein curr to head value for traverse
        curr = self.head
        pos = 0
        #loop run until the end
        while curr!=None:
            #if pos is equal to index return the data
            if pos == index:
                return curr.data
            #else care on
            curr = curr.next
            pos +=1
        return 'index error'
l = linkedlist()
l.inserthead(2)
l.inserthead(5)
l.inserthead(10)
l.inserthead(15)
l.inserthead(25)
l.inserthead(35)
l.append(45)
l.insert_after(5,6)
l.clear()
l.inserthead(2)
l.inserthead(5)
l.inserthead(10)
l.inserthead(15)
l.inserthead(25)
l.inserthead(35)
l.delete_head()
l.inserthead(45)
l.inserthead(6)
l.inserthead(4)
l.inserthead(456)
l.pop()
l.remove(45)
l.search(5)
l[2]
print(l)
