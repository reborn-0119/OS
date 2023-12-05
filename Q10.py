class Process:
    def __init__(self, process_id, priority, burst_time):
        self.process_id = process_id
        self.priority = priority
        self.burst_time = burst_time

def priority_scheduling(processes):
    # Sort processes based on priority
    processes.sort(key=lambda x: x.priority, reverse=True)

    # Calculate completion time, turnaround time, and waiting time
    completion_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    completion_time[0] = processes[0].burst_time

    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + processes[i].burst_time

    for i in range(len(processes)):
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - processes[i].burst_time

    # Print results
    print("Process\t Priority\t Burst Time\t Completion Time\t Turnaround Time\t Waiting Time")
    for i in range(len(processes)):
        print(f"{processes[i].process_id}\t\t {processes[i].priority}\t\t {processes[i].burst_time}\t\t "
              f"{completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

if __name__ == "__main__":
    # Example processes
    processes = [
        Process(1, 4, 6),
        Process(2, 2, 8),
        Process(3, 6, 7),
        Process(4, 8, 3)
    ]

    # Run Priority Scheduling
    priority_scheduling(processes)
