# def FCFS (AT,BT,PR):
#     ST =[]
#     FT = []
#     print("FCFS SELECTED....")
#     ST.append(AT[0])
#     FT.append(BT[0]+AT[0])  #FOR FIRST TIME
#     for X in range(1,len(AT)):
#         if(AT[X] <= FT[X-1]):
#             ST.append(FT[X-1])
#             FT.append(ST[X]+BT[X])
#         elif(AT[X] > FT[X-1]):
#             ST.append(AT[X])
#             FT.append(ST[X]+BT[X])
#     return AT,BT,PR,ST,FT  


def FCFS(arrival_time, burst_time, priority):
    n = len(arrival_time)
    
    # Sort processes based on arrival time
    processes = sorted(range(n), key=lambda i: arrival_time[i])
    
    # Initialize starting time and finishing time arrays
    starting_time = [0] * n
    finishing_time = [0] * n
    
    # Calculate starting time and finishing time for each process
    current_time = 0
    for i in range(n):
        process_id = processes[i]
        starting_time[process_id] = max(current_time, arrival_time[process_id])
        current_time = starting_time[process_id] + burst_time[process_id]
        finishing_time[process_id] = current_time
    
    return arrival_time , burst_time,priority, starting_time, finishing_time




