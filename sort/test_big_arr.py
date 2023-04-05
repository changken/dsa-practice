import numpy as np
# O(n^2)
from bubblesort import BubbleSort
from insertion_sort import InsertionSort
from selectionsort import SelectionSort

# O(nlogn)
from mergesort import MergeSort
from quicksort import QuickSort, LomutoPartition
from heapsort import HeapSort

# theta(n+k) O(n^2)
from bucketsort import BucketSort
# O(dn)
from radixsort import RadixSort
# O(n^2 ~ nlogn)
from shellsort import ShellSort

from print_data_array import PrintDataArray
import time


def main():
    np.random.seed(0)

    arr = np.random.randint(0, 10000, 10000).tolist()

    print("original: \n")
    PrintDataArray(arr)

    start = time.time()  # 起始
    # 跑不完
    # BubbleSort(arr)
    # SelectionSort(arr)
    # InsertionSort(arr)

    # 跑得完
    # MergeSort(arr, 0, len(arr) - 1) # 0.05 sec
    # QuickSort(arr, 0, len(arr) - 1, LomutoPartition) # 0.08 sec
    # HeapSort(arr) # 0.13 sec

    # BucketSort(arr) # 0.01 sec!!!!!
    # RadixSort(arr) # 0.05 sec
    ShellSort(arr)  # 0.12 sec

    end = time.time()  # 結束

    print("sorted: \n")
    PrintDataArray(arr)

    print("time: {0} sec".format(end - start))


if __name__ == "__main__":
    main()
