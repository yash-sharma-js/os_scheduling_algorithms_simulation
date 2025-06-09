# from tester import *

# # IN THIS FIRST WE HAVE TO SORT IT COMP... TO AT

# # THEN IN COMP... OF BT BUT START WITH 1ST INDEX NOT WITH 0TH

# def sjf_np(AT,BT):
#     DAT=[]
#     DBT=[]
#     dummyval(AT,BT,DAT,DBT)
#     for x in range(1,len(AT)):
#         for y in range(1,len(AT)):
#             if(BT[x] < BT[y]):
#                 TP=swap(AT,BT,x,y)
#                 AT=TP[0]
#                 BT=TP[1]


def sjf_preemptive(arrival_time, burst_time, priority):
    n = len(arrival_time)
    processes = list(range(n))
    
    # Initialize starting time and finishing time arrays
    starting_time = [0] * n
    finishing_time = [0] * n
    remaining_time = burst_time.copy()
    
    # Initialize a list to track remaining time of processes
    remaining_time = burst_time.copy()
    
    current_time = 0
    completed = 0
    
    # Loop until all processes are completed
    while completed < n:
        # Find process with shortest remaining time
        shortest = min([remaining_time[i] for i in processes if arrival_time[i] <= current_time])
        shortest_process = [i for i in processes if remaining_time[i] == shortest and arrival_time[i] <= current_time][0]
        
        # Update starting time and finishing time for the process
        starting_time[shortest_process] = current_time
        current_time += 1
        remaining_time[shortest_process] -= 1
        
        # Check if process is completed
        if remaining_time[shortest_process] == 0:
            finishing_time[shortest_process] = current_time
            processes.remove(shortest_process)
            completed += 1
    
    return arrival_time,burst_time,priority,starting_time, finishing_time