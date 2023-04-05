import math


def InterpolationSearch(arr: list[int], target: int) -> bool:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (target - arr[start]) * (end - start) // (arr[end] - arr[start]) + start

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1

    return False


def main():
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target = 43  # 40

    result = "{0}找到了!".format(target) if InterpolationSearch(
        arr, target) else "{0}沒找到!".format(target)
    print(result)


if __name__ == "__main__":
    main()
