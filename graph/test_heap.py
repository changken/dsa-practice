from prim_algorithm_heap import BinaryHeap, HeapNode
import math

if __name__ == "__main__":
    distance = [2, 1, 3, 4, 6, 5, 7]
    minQueue = BinaryHeap(len(distance))
    minQueue.BuildMinHeap(distance)
    minQueue.display()

    while not minQueue.IsHeapEmpty():
        u = minQueue.ExtractMin()
        print("current heap min: {0}".format(u))
        minQueue.display()
