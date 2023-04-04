import abc

# 遞迴版本 會有龐大的空間複雜度


def QuickSortRecursion(arr: list[int]):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return QuickSortRecursion(left) + [pivot] + QuickSortRecursion(right)


class PartitionInterface(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def Partition(arr: list[int], start: int, end: int) -> int:
        pass


class LomutoPartition(PartitionInterface):
    # 原地交換版本(In-Place)-Lomuto partition scheme
    def Partition(arr: list[int], start: int, end: int) -> int:
        pivot = arr[end]
        i = start - 1  # 比pivot小的元素最後一個index
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1  # 將i往後移
                arr[i], arr[j] = arr[j], arr[i]  # 將比pivot小的元素放在i

        i += 1  # 把i往後移到比pivot大的元素的第一個位置
        arr[i], arr[end] = arr[end], arr[i]  # 將piovt放在i
        return i


class HoarePartition(PartitionInterface):
    # 原地交換版本(In-Place)-Hoare partition scheme
    def Partition(arr: list[int], start: int, end: int) -> int:
        pivot = arr[end]
        left = start
        right = end - 1
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
            while arr[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[end], arr[left] = arr[left], arr[end]
        return left


def QuickSort(arr: list[int], start: int, end: int, partition: PartitionInterface) -> None:
    if start < end:
        # print(end)
        pivot = partition.Partition(arr, start, end)
        # print(pivot)
        QuickSort(arr, start, pivot - 1, partition)
        QuickSort(arr, pivot + 1, end, partition)


def PrintArray(arr: list[int]) -> None:
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    arr = [9, 4, 1, 6, 7, 3, 8, 2, 5]

    print("original: \n")
    PrintArray(arr)

    #QuickSort(arr, 0, len(arr) - 1, HoarePartition)
    arr = QuickSortRecursion(arr)

    print("sorted: \n")
    PrintArray(arr)


if __name__ == "__main__":
    main()
