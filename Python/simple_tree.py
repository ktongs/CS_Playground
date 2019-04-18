class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self,value,height = 0, left = 0, right = 0):
        if self.data is value:
            print('height:'+str(height),'left:'+str(left),'right:'+str(right))
            return True
        elif value < self.data:
            if self.left is not None:
                return self.left.search(value,height +1,left +1,right)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.search(value,height +1,left,right+1)
            else:
                return False

b = Node(10)
b.insert(5)
b.insert(15)
b.insert(12)
b.insert(8)
b.insert(4)
print(b.left.right.data)
print(b.search(8))
print(b.search(4))
print(b.search(10))
print(b.search(12))
print(b.search(11))


