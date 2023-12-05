import platform
import os

def get_kernel_version():
    return platform.uname().release

def get_cpu_type():
    return platform.processor()

def get_cpu_info():
    cpu_info = {}
    try:
        with open('/proc/cpuinfo', 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    cpu_info[key] = value
    except FileNotFoundError:
        return "Unable to fetch CPU information"

    if not cpu_info:
        return "No CPU information available"

    return cpu_info

if __name__ == "__main__":
    # Get and print kernel version
    kernel_version = get_kernel_version()
    print(f"Linux Kernel Version: {kernel_version}")

    # Get and print CPU type
    cpu_type = get_cpu_type()
    print(f"CPU Type: {cpu_type}")

    # Get and print CPU information
    cpu_info = get_cpu_info()

    if isinstance(cpu_info, str):
        print(cpu_info)
    else:
        print("\nCPU Information:")
        for key, value in cpu_info.items():
            print(f"{key}: {value}")
