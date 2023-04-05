from print_data_array import PrintDataArray


def ShellSort(arr: list[int]) -> None:
    n = len(arr)
    gap = n // 2  # 時間複雜度會因gap而有所不同，每次為原本的一半

    while gap > 0:
        for i in range(gap, n):  # 從gap~n
            temp = arr[i]  # 每個i為temp
            j = i  # j為i
            # 當j>=gap且arr[j-gap](前一半的element)>temp
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]  # j的值變為j-gap(前一半的element)
                j -= gap  # j減掉gap(往前跳一個gap)
            arr[j] = temp  # 最後j的值變為temp
        gap //= 2  # gap砍一半


def main():
    arr = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

    print("original: \n")
    PrintDataArray(arr)

    ShellSort(arr)

    print("sorted: \n")
    PrintDataArray(arr)


if __name__ == "__main__":
    main()
