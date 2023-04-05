import math


class Node:
    def __init__(self, key, value):
        self.key = key  # number
        self.value = value  # genre
        self.next = None  # pointer to remember memory address of next node


class HashChain_ll:
    def __init__(self, size):
        self.size = size  # size: size of table, count: number of data
        self.count = 0  # count/size = load factor
        # allocate the first dimension of table
        # initialization, ensure every slot points to None
        self.table = [None for _ in range(self.size)]

    def __del__(self):
        for i in range(self.size):  # visit every node in table
            # and release the memory of each node
            current = self.table[i]       # point current to first node in list
            while current is not None:   # traversal in list
                previous = current
                current = current.next
                del previous
                previous = None

        del self.table

    def hash_function(self, key):
        # Multiplication method
        A = 0.6180339887
        frac = key * A - math.floor(key * A)

        return math.floor(self.size * frac)

    def table_doubling(self):
        size_original = self.size  # size_orig represents the original size of table
        self.size *= 2  # double the size of table
        self.rehashing(size_original)  # create new table with new larger size

    def table_shrinking(self):
        size_original = self.size  # size_orig represents the original size of table
        self.size //= 2              # shrink the size of table
        # create new table with new smaller size
        self.rehashing(size_original)

    def rehashing(self, size_original):
        # allocate memory for new table
        # initialization, ensure every node in slot points to NULL
        new_table = [None for _ in range(self.size)]

        for i in range(size_original):  # visit every node in the original table
            # curr_orig: current node in original table
            current_original = self.table[i]
            previous_original = None  # prev_orig: following curr_orig

            while current_original is not None:  # traversal in list of each slot in original table
                # curr_orig will be directly move to new table
                previous_original = current_original.next
                # need prev_orig to keep pointer in original table

                # get index of slot in new table
                index = self.hash_function(current_original.key)

                # push_front(), do not allocate new memory space for data
                # directly move node in original table to new table
                if new_table[index] is None:  # means new_table[index] is empty
                    new_table[index] = current_original
                    # equivalent to curr_orig->next = 0
                    new_table[index].next = None

                # if there is no initialization for new_table, segmentation faults might happen
                # because new_table[index] might not point to None
                # but new_table[index] is empty
                else:
                    # if new_table[index] is not empty
                    next_node = new_table[index].next  # push_front()
                    new_table[index].next = current_original
                    current_original.next = next_node

                # visit the next node in list in original table
                current_original = previous_original

        del self.table  # release memory of original table
        self.table = new_table  # point table of object to new table

    def insert(self, node):  # consider table_doubling()
        self.count += 1
        if self.count > self.size:  # consider load factor
            self.table_doubling()  # if n/m > 1, then double the size of table

        index = self.hash_function(node.key)  # get index of slot
        new_node = node  # create new node to store data

        # push_front()
        if self.table[index] is None:  # eg: list: (empty), add 4
            self.table[index] = new_node  # eg: list: 4->NULL
        else:
            # eg: list: 5->9->NULL  , add 4
            next_node = self.table[index].next  # list: 5->4->9->NULL
            self.table[index].next = new_node
            new_node.next = next_node

    def delete(self, key):  # consider table_shrinking()
        index = self.hash_function(key)  # get index of slot
        current = self.table[index]  # use two pointer for traversal in list
        previous = None

        while current is not None and current.key != key:
            previous = current
            current = current.next

        # 1. data not found
        # 2. data found at first node in list
        # 3. data found at other position in list

        if current is None:  # eg: list:5->2->9->NULL, want to delete 3
            print("Data not found.\n")
            return
        else:
            if previous is None:  # eg: list:5->2->9->NULL, want to delete 5
                # after deleting 5, list:2->9->NULL
                self.table[index] = current.next
                # current points to 5
            else:
                # eg: list:5->2->9->NULL, want to delete 2
                previous.next = current.next  # after deleting 2, list:5->9->NULL
                # current points to 2
            del current
            current = None

        self.count -= 1

        if self.count < self.size / 4:  # consider load factor
            self.table_shrinking()  # if n/m < 4, then shrink the table

    def search(self, key):
        index = self.hash_function(key)  # get index of slot
        current = self.table[index]  # current points to the first node in list

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return "\n no such data"

    def display_table(self):
        for i in range(self.size):  # visit every node in table
            print("#slot#{0}:".format(i))
            current = self.table[i]
            while current is not None:
                print("(k={0}, v={1})".format(
                    current.key, current.value), end=" ")
                current = current.next
            print()
        print()


def main():
    hash = HashChain_ll(2)

    hash.insert(Node(12, "post rock"))
    hash.insert(Node(592, "shoegaze"))
    print("After inserting key(12),key(592):\n")
    hash.display_table()

    hash.insert(Node(6594, "blues"))    # evoke TableDoubling()
    print("After inserting key(6594), evoke TableDoubling():\n")
    hash.display_table()
    hash.insert(Node(7, "folk"))
    print("After inserting key(7):\n")
    hash.display_table()

    hash.insert(Node(123596, "hiphop"))     # evoke TableDoubling()
    print("After inserting key(123596), evoke TableDoubling():\n")
    hash.display_table()
    hash.insert(Node(93, "soul"))
    hash.insert(Node(2288, "indie"))
    hash.insert(Node(793, "jazz"))
    print("After inserting key(93),key(2288),key(793):\n")
    hash.display_table()

    hash.insert(Node(8491, "electro"))      # evoke TableDoubling()
    print("After inserting key(8491), evoke TableDoubling():\n")
    hash.display_table()
    hash.insert(Node(323359, "pop"))
    print("After inserting key(323359):\n")
    hash.display_table()

    print("Searching: genre(8491) is ", hash.search(8491), ".\n\n")
    print("Searching: genre(7) is ", hash.search(7), ".\n\n")

    hash.delete(7)
    print("After deleting key(7):\n")
    print("Searching: genre(7) is ", hash.search(7), ".\n\n")

    hash.delete(592)
    print("After deleting key(592):\n")
    hash.display_table()

    print("Want to  delete key(592) again:\n")
    hash.delete(592)

    hash.delete(123596)
    hash.delete(323359)
    hash.delete(793)
    hash.delete(93)
    print("After deleting key(123596),key(323359),key(793),key(93):\n")
    hash.display_table()

    hash.delete(6594)      # evoke TableShrinking()
    print("After deleting key(6594), evoke TableShrinking():\n")
    hash.display_table()


if __name__ == "__main__":
    main()
