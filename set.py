def FindSetCollapsing(subset: list[int], i: int):
    # 找到每一個element的root
    root = i
    while subset[root] >= 0:
        root = subset[root]

    # 進行collapsing
    while i != root:
        parent = subset[i]
        subset[i] = root
        i = parent

    return root


def UnionSet(subset: list[int], x: int, y: int):
    x_root = FindSetCollapsing(subset, x)
    y_root = FindSetCollapsing(subset, y)

    '''
    用rank比較, 負越多表示set越多element, 所以是值比較小的element比較多
    x_root, y_root的subset[]一定都是負值

    x比較多element或是一樣多的時候, 以x作為root
    '''
    if subset[x_root] <= subset[y_root]:
        subset[x_root] += subset[y_root]
        subset[y_root] = x_root
    else:  # subset[x_root] > subset[y_root], 表示y比較多element
        subset[y_root] += subset[x_root]
        subset[x_root] = y_root


def PrintArray(array: list[int]) -> None:
    for i in range(len(array)):
        print("   {0}".format(i), end=' ')
    print()

    for i in range(len(array)):
        print("   {0}".format(array[i]), end=' ')
    print()


class main():
    array = [-1, -1, -1, -1, -1, -1]
    PrintArray(array)

    UnionSet(array, 1, 2)
    print("After union(1,2):\n")
    PrintArray(array)

    UnionSet(array, 0, 2)
    print("After union(0,2):\n")
    PrintArray(array)

    UnionSet(array, 3, 5)
    print("After union(3,5):\n")
    PrintArray(array)

    UnionSet(array, 2, 5)
    print("After union(2,5):\n")
    PrintArray(array)

    print("element(5) belongs to Set({0}).\n".format(
        FindSetCollapsing(array, 5)))
    print("After collapsing:\n")
    PrintArray(array)


if __name__ == '__main__':
    main()
