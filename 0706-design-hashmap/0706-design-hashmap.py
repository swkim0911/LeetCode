class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        ans = self.dict.get(key)
        if ans is None:
            return -1
        else:
            return ans

    def remove(self, key: int) -> None:
        tmp = self.dict.get(key)
        if tmp is not None:
            self.dict.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)