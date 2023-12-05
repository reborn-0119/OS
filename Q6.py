import psutil

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        'total_memory': memory.total,
        'free_memory': memory.free,
        'used_memory': memory.used
    }

if __name__ == "__main__":
    # Get and print memory information
    memory_info = get_memory_info()

    print("Memory Information:")
    print(f"Total Memory: {memory_info['total_memory'] / (1024 ** 3):.2f} GB")
    print(f"Free Memory: {memory_info['free_memory'] / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory_info['used_memory'] / (1024 ** 3):.2f} GB")
