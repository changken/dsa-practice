# O(n)
def LinearSearch(arr: list[int], target: int) -> bool:
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False


def main():
    arr = [75, 50, 60, 20, 90, 40, 80]
    target = 20

    result = "{0}找到了!".format(target) if LinearSearch(arr, target) else "{0}沒找到!".format(target) 
    print(result)


if __name__ == "__main__":
    main()
