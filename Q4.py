import os
import multiprocessing

def same_code():
    print("Both parent and child executing the same code.")
    print(f"Process ID: {os.getpid()}")
    print(f"Parent Process ID: {os.getppid()}")

def different_code():
    print("Both parent and child executing different code.")
    print(f"Process ID: {os.getpid()}")
    print(f"Parent Process ID: {os.getppid()}")

def wait_for_child():
    print("Parent waiting for the child to finish.")
    print(f"Process ID (Parent): {os.getpid()}")

    child_pid = os.fork()

    if child_pid == 0:
        same_code()  # Child process executes the same code
        os._exit(0)
    else:
        os.wait()  # Parent waits for the child to finish
        different_code()  # Parent executes different code

if __name__ == "__main__":
    print("Parent process is running.")
    print(f"Process ID (Parent): {os.getpid()}")

    wait_for_child()
