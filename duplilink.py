class Node:
    def __init__(self, data):        
        self.data = data
        self.next = None
    
class Link:
    def __init__(self):
        self.head = None
    def inser(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastNode = self.head
            while(True):
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newnode
    def printlist(self, head):
        curr = self.head
        while(True):
            print(curr.data)
            curr=curr.next

nn = Node("k")
duplilink = Link()
duplilink.inser(nn)
n2 = Node("a")
duplilink.inser(n2)
n3 = Node("r")
duplilink.inser(n3)
n4 = Node("t")
duplilink.inser(n4)
n5 = Node("i")
duplilink.inser(n5)
n6 = Node("k")
duplilink.inser(n6)
duplilink.printlist()

                




        


# nn = Node("Ka")


