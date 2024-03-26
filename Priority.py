# from tester import * 




# def priority(AT,BT):
#     pass

def priority_non_preemptive(arrival_time, burst_time, priority):
    n = len(arrival_time)
    
    # Initialize starting time, finishing time, and remaining burst time arrays
    starting_time = [0] * n
    finishing_time = [0] * n
    remaining_time = burst_time.copy()
    
    # Sort processes based on priority (lower value has higher priority)
    processes = sorted(range(n), key=lambda i: priority[i])
    
    current_time = 0
    completed = 0
    
    # Loop until all processes are completed
    while completed < n:
        selected_process = None
        selected_priority = float('inf')
        
        # Find the process with the highest priority among the arrived processes
        for i in processes:
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                if priority[i] < selected_priority:
                    selected_priority = priority[i]
                    selected_process = i
        
        # Update starting time and finishing time for the selected process
        starting_time[selected_process] = current_time
        current_time += burst_time[selected_process]
        finishing_time[selected_process] = current_time
        remaining_time[selected_process] = 0
        completed += 1
        
        # Remove the selected process from the list of processes
        processes.remove(selected_process)
    
    # Return starting time, finishing time, arrival time, and burst time for each process
    return arrival_time,burst_time,priority,starting_time, finishing_time