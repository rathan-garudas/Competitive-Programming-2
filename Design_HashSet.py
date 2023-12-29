#TC - Insert - O(1)
#     Remove - O(1)
#     Search - O(1)
class MyHashSet:

    def __init__(self):
        self.no_buckets = 1000
        self.bucketSize = 1000
        self.hashSet = [None]*self.no_buckets

    def hashFun1(self, key):
        return key%self.no_buckets
    
    def hashFun2(self, key):
        return key//self.bucketSize

    def add(self, key: int) -> None:
        idx = self.hashFun1(key)
        bucket_idx = self.hashFun2(key)
        if self.hashSet[idx] == None:
            if idx == 0:
                self.hashSet[idx] = [False] * (self.bucketSize + 1)
            else:
                self.hashSet[idx] = [False] * self.bucketSize
        self.hashSet[idx][bucket_idx] = True

    def remove(self, key: int) -> None:
        idx = self.hashFun1(key)
        bucket_idx = self.hashFun2(key)
        if self.hashSet[idx] == None:
            return
        self.hashSet[idx][bucket_idx] = False

    def contains(self, key: int) -> bool:
        idx = self.hashFun1(key)
        bucket_idx = self.hashFun2(key)
        if self.hashSet[idx] == None:
            return False
        return self.hashSet[idx][bucket_idx]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)