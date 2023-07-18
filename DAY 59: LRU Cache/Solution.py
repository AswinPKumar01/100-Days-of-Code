class DLL:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.head = DLL(0,0)
        self.tail = DLL(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
           
            node = self.dict[key]
        
            node.prev.next = node.next
            node.next.prev = node.prev
    
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            return node.val
     
        else:
            return -1


    def put(self, key: int, value: int) -> None:
       
        if key in self.dict:
           
            self.get(key)
      
            self.dict[key].val = value
            return
        

        
        self.size +=1
        if self.size > self.capacity:
            lru = self.tail.prev
            del self.dict[lru.key]
            lru.prev.next = lru.next
            lru.next.prev = lru.prev
            self.size -= 1
 
        new_head = DLL(key, value)
        self.head.next.prev = new_head
        new_head.next = self.head.next
        self.head.next = new_head
        new_head.prev = self.head
        self.dict[key] = new_head

        
    
