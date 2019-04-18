class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1 *10)
b = Node(2 * 10)
c = Node(3 * 10)
d = Node(4 * 10)

a.next = b
b.next = c
c.next = d

# print(a.next.next.data)

def countNodes(head):
    count = 1
    temp = head.next
    while temp != None:
        count += 1
        temp = temp.next
    return count

# print(countNodes(a))

class LinkedList():
    def __init__(self,node):
        self.head = node

    def append(self,data):
        node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = node

    def search(self,data):
        curr = self.head

        if curr.data == data:
            return 0

        count = 1

        while curr.next != None:
            if curr.next.data == data:
                return count
            count += 1
            curr = curr.next
        return False

myList = LinkedList(a)
myList.append(10)
myList.append(90)

print(d.next.next.data)

print(myList.search(90))
print(myList.search(40))
print(myList.search(-1))