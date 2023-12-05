import threading

def calculate_sum(start, end, result):
    partial_sum = sum(range(start, end + 1))
    result.append(partial_sum)

if __name__ == "__main__":
    n = 10  # Change this to the desired number of elements

    num_threads = 4  # Change this to the desired number of threads
    chunk_size = n // num_threads

    threads = []
    result = []

    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_threads - 1 else n

        thread = threading.Thread(target=calculate_sum, args=(start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_sum = sum(result)
    print(f"Sum of first {n} numbers: {final_sum}")
