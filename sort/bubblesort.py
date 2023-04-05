def BubbleSort(arr: list[int]) -> None:
    n = len(arr)
    while n > 1: 
        n -= 1 # 慢慢將最大值移到n處，所以每個loop n會-1
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


def PrintArray(arr: list[int]) -> None:
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    arr = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

    print("original: \n")
    PrintArray(arr)

    BubbleSort(arr)

    print("sorted: \n")
    PrintArray(arr)


if __name__ == "__main__":
    main()
