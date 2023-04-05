from print_data_array import PrintDataArray


def SelectionSort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        min = i  # 每次假定i為最小值
        for j in range(i+1, n):  # loop i+1 ~ n
            if arr[j] < arr[min]:  # 如果有比i小的值，更新min為j
                min = j
        if min != i:  # 如果min不是i，則交換i與min的值
            arr[i], arr[min] = arr[min], arr[i]


def PrintArray(arr: list[int]) -> None:
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    arr = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

    print("original: \n")
    PrintDataArray(arr)

    SelectionSort(arr)

    print("sorted: \n")
    PrintDataArray(arr)


if __name__ == "__main__":
    main()
