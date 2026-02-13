import math
import time
from multiprocessing import Pool, cpu_count, freeze_support

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factoril(n):
    return math.factorial(n)


if __name__ == "__main__":
    freeze_support()   # required on Windows

    # ---------------- SEQUENTIAL ----------------
    starttime1 = time.time()
    seq_results = []

    for num in numbers:
        result = compute_factoril(num)
        seq_results.append(result)
        print(f"sequential: Factorial {num} calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential time: {seqtime}")


    # ---------------- PARALLEL ----------------
    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factoril, numbers)

    for num in numbers:
        print(f"multiprocessing: Factorial {num} calculated")

    paralleltime = time.time() - starttime2
    print(f"\nParallel time: {paralleltime}")
