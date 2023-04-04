import math


def MergeSort(arr: list[int], start: int, end: int) -> None:
    if start < end:  # front與end為矩陣範圍 #表示目前的矩陣範圍是有效的
        mid = (start + end) // 2  # mid即是將矩陣對半分的index
        MergeSort(arr, start, mid)  # 繼續divide矩陣的前半段subarray
        MergeSort(arr, mid + 1, end)  # 繼續divide矩陣的後半段subarray
        Merge(arr, start, mid, end)  # 將兩個subarray做比較, 並合併出排序後的矩陣


def Merge(arr: list[int], start: int, mid: int, end: int) -> None:
    # 利用 list,
    # 把array[front]~array[mid]放進 leftSub[]
    # 把array[mid+1]~array[end]放進 rightSub[]
    leftSub = arr[start:mid+1]
    rightSub = arr[mid+1:end+1]
    leftSub.append(math.inf)  # 在leftSub[]尾端加入值為 無窮大 的元素
    rightSub.append(math.inf)  # 在rightSub[]尾端加入值為 無窮大 的元素

    left = 0
    right = 0

    for i in range(start, end+1):
        if leftSub[left] <= rightSub[right]:
            arr[i] = leftSub[left]
            left += 1
        else:
            arr[i] = rightSub[right]
            right += 1


def PrintArray(arr: list[int]) -> None:
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    arr = [5, 3, 8, 6, 2, 7, 1, 4]

    print("original: \n")
    PrintArray(arr)

    MergeSort(arr, 0, len(arr)-1)

    print("sorted: \n")
    PrintArray(arr)


if __name__ == "__main__":
    main()
