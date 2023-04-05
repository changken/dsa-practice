from print_data_array import PrintDataArray


def RadixSort(arr: list[int]):
    max_num = max(arr)  # 陣列最大值
    digits = 1

    # 當最大值大於10次方時
    while max_num >= 10 ** digits:
        digits += 1

    # 根續LSD(Least Significant Digit First)來對於每個元素來放入桶子排序
    for i in range(digits):
        # 產生空桶子
        buckets = [[] for _ in range(10)]

        # 根據位數大小分類
        for j in arr:
            # radix為j / 10次方再取10的餘數
            radix = int(j / (10 ** i) % 10)
            buckets[radix].append(j)

        # 合併桶子的資料
        x = 0  # 以x來控制arr的索引
        for y in range(10):  # 依序取出桶子
            for num in buckets[y]:  # 取出該桶子的資料
                arr[x] = num  # 將資料依序放入arr
                x += 1

    return arr


def main():
    arr = [28, 96, 5, 33, 60, 169, 170, 249, 362, 44, 84, 123]

    print("original: \n")
    PrintDataArray(arr)

    RadixSort(arr)

    print("sorted: \n")
    PrintDataArray(arr)


if __name__ == '__main__':
    main()
