# O(log n)
def BinarySearch(arr: list[int], target: int) -> bool:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1

    return False


def main():
    arr = [10, 15, 25, 40, 45, 55, 60, 80, 90]
    target = 12  # 55
    # arr = [75, 50, 60, 20, 90, 40, 80]
    # target = 20

    result = "{0}找到了!".format(target) if BinarySearch(
        arr, target) else "{0}沒找到!".format(target)
    print(result)


if __name__ == "__main__":
    main()
