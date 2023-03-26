from numba import cuda

def cpu_print():
    print("cpu print")

@cuda.jit
def gpu_print():
    print("gpu print")

def main():
    print(cuda.gpus)

    gpu_print[1,2]()
    cuda.synchronize()
    cpu_print()

if __name__ == "__main__":
    main()