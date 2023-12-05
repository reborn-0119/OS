def first_fit(memory, process_size):
    for i in range(len(memory)):
        if memory[i] >= process_size:
            memory[i] -= process_size
            return i
    return -1

def best_fit(memory, process_size):
    best_fit_index = -1
    best_fit_size = float('inf')

    for i in range(len(memory)):
        if memory[i] >= process_size and memory[i] - process_size < best_fit_size:
            best_fit_index = i
            best_fit_size = memory[i] - process_size

    if best_fit_index != -1:
        memory[best_fit_index] -= process_size

    return best_fit_index

def worst_fit(memory, process_size):
    worst_fit_index = -1
    worst_fit_size = -1

    for i in range(len(memory)):
        if memory[i] >= process_size and memory[i] > worst_fit_size:
            worst_fit_index = i
            worst_fit_size = memory[i]

    if worst_fit_index != -1:
        memory[worst_fit_index] -= process_size

    return worst_fit_index

def display_memory(memory):
    for i in range(len(memory)):
        print(f"Block {i}: {memory[i]} KB")


memory_size = int(input("Enter the total memory size (in KB): "))
num_blocks = int(input("Enter the number of memory blocks: "))
memory = [memory_size // num_blocks] * num_blocks

while True:
    print("\nMemory Allocation Strategies:")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")
    print("4. Display Memory Blocks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        process_size = int(input("Enter the process size (in KB): "))
        index = first_fit(memory, process_size)
        if index != -1:
            print(f"Allocated {process_size} KB to Block {index}")
        else:
            print("Memory allocation failed. No suitable block found.")

    elif choice == 2:
        process_size = int(input("Enter the process size (in KB): "))
        index = best_fit(memory, process_size)
        if index != -1:
            print(f"Allocated {process_size} KB to Block {index}")
        else:
            print("Memory allocation failed. No suitable block found.")

    elif choice == 3:
        process_size = int(input("Enter the process size (in KB): "))
        index = worst_fit(memory, process_size)
        if index != -1:
            print(f"Allocated {process_size} KB to Block {index}")
        else:
            print("Memory allocation failed. No suitable block found.")

    elif choice == 4:
        display_memory(memory)

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
