from collections import deque


class my_dict:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashChain_std:
    def __init__(self, size):
        self.size = size  # size of table
        self.count = 0  # count: number of data
        # hash table with linked list
        # allocate memory for each slot
        self.table = [deque() for _ in range(size)]

    def preHashing(self, key_str):  # turn string_type_key to int_type_key
        # if   key_str = Jordan, exp = 9
        # then key_int = ASCII(J)*9 ^ 5+ASCII(o)*9 ^ 4+ASCII(r)*9 ^ 3
        #               +ASCII(d)*9 ^ 2+ASCII(a)*9 ^ 1+ASCII(n)*9 ^ 0

        exp = 9  # choose randomly
        key_int = 0
        p = 1

        for i in range(len(key_str)-1, -1, -1):
            key_int += ord(key_str[i]) * p
            p *= exp

        return key_int

    def hashFunction(self, key_str):  # using Division method
        return self.preHashing(key_str) % self.size

    def insert(self, my_dict_obj):
        # two steps: 1. get index from hash function
        #            2. insert data at the front of linked list

        index = self.hashFunction(my_dict_obj.key)
        selected_list = self.table[index]
        selected_list.appendleft(my_dict_obj)
        self.count += 1

    def delete(self, key_str):
        # two steps: 1. get index from hash function
        #            2. traversal in linked list

        index = self.hashFunction(key_str)
        selected_list = self.table[index]
        for itr in selected_list:
            if itr.key == key_str:
                selected_list.remove(itr)
                self.count -= 1
                return

    def search(self, key_str):
        # two steps: 1. get index from hash function
        #            2. traversal in linked list
        index = self.hashFunction(key_str)
        selected_list = self.table[index]
        for itr in selected_list:
            if itr.key == key_str:
                return itr.value

        return "No such data"

    def displayTable(self):
        for i in range(self.size):
            print("slot#{0}".format(i), end=": ")
            selected_list = self.table[i]

            for itr in selected_list:
                print("(k={0}, v={1})".format(itr.key, itr.value), end=" ")
            print()
        print()


def main():
    hash = HashChain_std(5)
    hash.insert(my_dict("T-Mac", "Magic"))
    hash.insert(my_dict("Bryant", "Lakers"))
    hash.insert(my_dict("Webber", "Kings"))
    hash.insert(my_dict("Arenas", "Wizards"))
    hash.insert(my_dict("Davis", "Clippers"))
    hash.insert(my_dict("Kidd", "Nets"))
    hash.displayTable()

    print("T-Mac is in {0}.".format(hash.search("T-Mac")))
    print("Arenas is in {0}.".format(hash.search("Arenas")))

    hash.delete("Kidd")
    hash.delete("T-Mac")
    print("\nAfter deleing Kidd and T-Mac:\n")
    hash.displayTable()


if __name__ == "__main__":
    main()
