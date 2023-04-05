import math


def BucketSort(arr: list[int]) -> None:
    max_x = max(arr)  # 找出最大值
    min_n = min(arr)  # 找出最小值
    size = 5

    # 依照arr元素的範圍/bucket數量來建立bucket
    buckets = [[] for _ in range(math.floor((max_x - min_n) / size) + 1)]

    n = len(arr)

    # 將每個元素放入bucket O(n)
    for i in range(n):
        val = arr[i]
        buckets[math.floor((val - min_n) / size)].append(val)

    result = []

    # O(k)
    for i in range(len(buckets)): 
        buckets[i] = sorted(buckets[i])  # 將每個bucket內的元素做排序

        result.extend(buckets[i])  # 將每個bucket內的元素放入result

    return result


def PrintArray(arr: list[int]) -> None:
    for i in range(len(arr)):
        print("   {0}".format(arr[i]), end=" ")
    print()


def main():
    arr = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]

    print("original: \n")
    PrintArray(arr)

    arr = BucketSort(arr)

    print("sorted: \n")
    PrintArray(arr)


if __name__ == "__main__":
    main()
