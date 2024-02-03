class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
    def __init__(self) -> None:
    #   points to head of linked list
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next

        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        pass
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        pass
        # Remove first node that contains data

if __name__ == "__main__":
   ll = LinkedList() # <__main__.LinkedList object at 0x1071aa9b0>
   ll.insert_at_beginning(15)
   ll.insert_at_beginning(345)
   ll.insert_at_beginning(5)
   ll.insert_at_beginning(89)
   ll.print()
   ll.remove_at(2)
   ll.insert_at(0,"27")
   ll.print()
   print("length:", ll.get_length())