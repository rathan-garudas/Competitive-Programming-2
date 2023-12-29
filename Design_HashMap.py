class MyHashMap:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None


    def __init__(self):
        self.hash = [self.Node(-1,-1)]*10000

    def hashFun(self, key):
        return key % 10000

    def findKey(self, node, key):
        prev = None
        curr = node

        while curr != None and curr.key != key:
            prev = curr
            curr = curr.next
        return prev

    def put(self, key: int, value: int) -> None:
        idx = self.hashFun(key)
        prev = self.findKey(self.hash[idx], key)

        if prev.next == None:
            prev.next = self.Node(key, value)
        else:
            prev.next.val = value
        return None

    def get(self, key: int) -> int:
        idx = self.hashFun(key)
        prev = self.findKey(self.hash[idx], key)

        if prev.next == None:
            return -1
        return prev.next.val

    def remove(self, key: int) -> None:
        idx = self.hashFun(key)
        prev = self.findKey(self.hash[idx], key)

        if prev.next == None:
            return -1
        prev.next = prev.next.next
        return None        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)