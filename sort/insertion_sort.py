def insertionSort(arr: list[int]):
    for i in range(1, len(arr)):
        key = arr[i]  # 檢查目前的key
        j = i - 1  # j等於i-1個元素
        # 如果key比arr[j]小 且 j >= 0
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]  # 將arr[j]往後移
            j -= 1
        arr[j+1] = key  # 如果j超出範圍 或 key > arr[j]


def printDataArray(arr: list[int]):
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    array = [5, 3, 1, 2, 6, 4]

    print("original: \n")
    printDataArray(array)

    insertionSort(array)

    print("sorted: \n")
    printDataArray(array)


if __name__ == "__main__":
    main()
