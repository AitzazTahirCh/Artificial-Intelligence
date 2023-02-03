#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


# In[17]:


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = None
    
    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next
        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str
    
    def push(self,val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head 
        while last.next is not None:
            last = last.next
            
        last.next = new_node


# In[127]:


list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
print(list)


# In[34]:


def pop(self):
    if self.head is None:
        raise Exception("Cannot pop --No Value--")
    
    temp = self.head
    if temp.next is None:
        self.head = None
        return
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None

LinkedList.pop = pop


# In[37]:


list.pop()
print(list)


# In[148]:


def remove(self, index):
    i = 0
    if self.head is None:
        raise Exception("Cannot remove --Linked List is empty--")
    
    temp = self.head
    
    if index == 0:
        self.head = None
    prev = temp
    temp = self.head
    while temp.next is not None:
        if(index == i):
            temp.next = temp.next.next
        i = i+1
        temp=temp.next
        
LinkedList.remove = remove


# In[149]:


print(list)
list.remove(1)
print(list)


# In[77]:


def insert(self, index, val):
    new_node = Node(val)
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    temp = self.head
    
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
        
    prev.next = new_node
    new_node.next = temp

LinkedList.insert = insert


# In[150]:


print(list)
list.insert(1, 20)
list.insert(1, 30)
print(list)


# In[ ]:





# In[116]:


class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ' - '.join(str(i) for i in self.queue)
        return myString
    
    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.size


    def enqueue(self, item):
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            raise Exception('Queue is Full!')

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            raise Exception('Queue is Empty!')


# In[151]:


myQueue = Queue(10)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue)


# In[152]:


myQueue.dequeue()
print(myQueue)


# In[153]:


myQueue.enqueue(4)
print(myQueue)


# In[ ]:





# In[ ]:




