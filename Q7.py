import subprocess

def copy_file(source, destination):
    try:
        subprocess.run(['copy', source, destination], check=True, shell=True)
        print(f"File copied successfully from {source} to {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    source_file = r'D:\\SEM-lll\\os\\Practical mains\\Source(Q7).txt'  # Use raw string to handle backslashes
    destination_file = r'D:\\SEM-lll\\os\\Practical mains\\Destination(Q7).txt'

    copy_file(source_file, destination_file)

