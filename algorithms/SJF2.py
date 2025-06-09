# from tester import *

# # IN THIS FIRST WE HAVE TO SORT IT COMP... TO AT

# # THEN IN COMP... OF BT BUT START WITH 1ST INDEX NOT WITH 0TH

# def sjf_p(AT,BT):
#     DAT=[]
#     DBT=[]
#     dummyval(AT,BT,DAT,DBT)
#     for x in range(1,len(AT)):
#         for y in range(1,len(AT)):
#             if(BT[x] < BT[y]):
#                 TP=swap(AT,BT,x,y)
#                 AT=TP[0]
#                 BT=TP[1]

def sjf_non_preemptive(arrival_time, burst_time, priority):
    n = len(arrival_time)
    processes = list(range(n))
    
    # Initialize starting time, finishing time, and priority arrays
    starting_time = [0] * n
    finishing_time = [0] * n
    
    # Sort processes based on arrival time
    processes.sort(key=lambda i: arrival_time[i])
    
    current_time = 0
    completed = 0
    
    # Loop until all processes are completed
    while completed < n:
        shortest_process = None
        shortest_burst_time = float('inf')
        
        # Find process with shortest burst time among arrived processes
        for i in processes:
            if arrival_time[i] <= current_time:
                if burst_time[i] < shortest_burst_time:
                    shortest_burst_time = burst_time[i]
                    shortest_process = i
        
        # Update starting time and finishing time for the process
        starting_time[shortest_process] = current_time
        current_time += burst_time[shortest_process]
        finishing_time[shortest_process] = current_time
        processes.remove(shortest_process)
        completed += 1
    
    # Return starting time, finishing time, arrival time, burst time, and priority for each process
    return arrival_time,burst_time,priority,starting_time, finishing_time