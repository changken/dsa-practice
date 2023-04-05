from print_data_array import PrintDataArray

def MaxHeapify(arr: list[int], root: int, length: int) -> None:
    left = 2 * root  # 取得left child
    right = 2 * root + 1  # 取得right child

    # largest用來記錄包含root與child, 三者之中Key最大的node
    if left <= length and arr[left] > arr[root]:
        largest = left
    else:
        largest = root

    if right <= length and arr[right] > arr[largest]:
        largest = right

    if largest != root:  # 如果目前root的Key不是三者中的最大
        # 就調換root與三者中Key最大的node之位置
        arr[root], arr[largest] = arr[largest], arr[root]
        MaxHeapify(arr, largest, length)  # 調整新的subtree成Max Heap


def BuildMaxHeap(arr: list[int]) -> None:
    for i in range(len(arr) // 2, 0, -1):
        MaxHeapify(arr, i, len(arr) - 1)  # length要減一, 因為heap從1開始存放資料


def HeapSort(arr: list[int]) -> None:
    arr.insert(0, 0)  # 將index(0)閒置

    BuildMaxHeap(arr)  # 將array調整成Max Heap

    size = len(arr) - 1  # size用來記錄「目前要處理的矩陣」之長度
    for i in range(size, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]  # 將最大值放到array的最後一個位置
        size -= 1  # size減一
        MaxHeapify(arr, 1, size)  # 調整「忽略最後一個位置」的矩陣，因其為max值

    arr.pop(0)  # 將index(0)刪除

def main():
    arr = [9, 4, 1, 6, 7, 3, 8, 2, 5]

    print("original: \n")
    PrintDataArray(arr)

    HeapSort(arr)

    print("sorted: \n")
    PrintDataArray(arr)

if __name__ == "__main__":
    main()
    