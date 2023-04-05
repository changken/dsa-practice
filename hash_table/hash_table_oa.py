class MyDict:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashOpenAddress:
    def __init__(self, size=0):
        self.size = size
        self.count = 0
        self.table = [MyDict("", "") for i in range(self.size)]

    def quadraticProbing(self, key, i):
        # c1 = c2 = 0.5
        return int(((key % self.size) + 0.5 * i + 0.5 * i ** 2) % self.size)

    def insert(self, key, value):
        i = 0
        while i != self.size:
            j = self.quadraticProbing(key, i)
            if self.table[j].key == "":
                self.table[j] = MyDict(key, value)
                self.count += 1
                return
            else:
                i += 1

    def delete(self, key):
        i = 0
        while i != self.size:
            j = self.quadraticProbing(key, i)
            if self.table[j].key == key:
                self.table[j] = MyDict("", "")
                self.count -= 1
                return
            else:
                i += 1

    def search(self, key):
        i = 0
        while i != self.size:
            j = self.quadraticProbing(key, i)
            if self.table[j].key == key:
                return self.table[j].value
            else:
                i += 1

        return None

    def display(self):
        for i in range(self.size):
            print("slot#{0}: (k={1}, v={2})".format(
                i, self.table[i].key, self.table[i].value
            ))
        print()


def main():
    hash = HashOpenAddress(8)  # probing sequence
    hash.insert(33, "blue")          # 1,2,4,7,3,0,6,5 -> 1
    hash.insert(10, "yellow")        # 2,3,5,0,4,1,7,6 -> 2
    hash.insert(77, "red")           # 5,6,0,3,7,4,2,1 -> 5
    hash.insert(2, "white")          # 2,3,5,0,4,1,7,6 -> 3
    hash.display()
    hash.insert(8, "black")          # 0,1,3,6,2,7,5,4 -> 0
    hash.insert(47, "gray")          # 7,0,2,5,1,6,4,3 -> 7
    hash.insert(90, "purple")        # 2,3,5,0,4,1,7,6 -> 4
    hash.insert(1, "deep purple")    # 4,5,7,2,6,3,1,0 -> 6
    hash.display()
    hash.insert(15, "green")         # hash table overflow

    print("number#90 is {0}\n\n".format(hash.search(90)))

    hash.delete(90)
    print("after deleting (90, purple):\n")
    print("number#90 is {0}\n".format(hash.search(90)))

    hash.insert(12, "orange")        # 4,5,7,2,6,3,1,0 -> 4
    hash.display()


if __name__ == "__main__":
    main()
