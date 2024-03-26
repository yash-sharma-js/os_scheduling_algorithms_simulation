# from tester import *


# def rnd_rbin(AT,BT,PR,Q):
#    x=-1                         #for indexing
#    y=AT.length                  # checking if burst of every process is completed or not
#    AT,BT,PR=sorting(AT,BT,PR)
#    DAT,DBT=dummyval(AT,BT)      #creating another array to make changes

#    while True:
#       x+=1
#       if(y == 0):      #checking if 
#         break
#       if DBT[x] - Q > 0:
#          DBT[x]=DBT[x] - Q
#          continue

def round_robin(arrival_time, burst_time, priority, time_quantum=3):
   n = len(arrival_time)
   processes = list(range(n))
   
   # Initialize starting time, finishing time, and remaining burst time arrays
   starting_time = [0] * n
   finishing_time = [0] * n
   remaining_time = burst_time.copy()
   
   # Initialize queue to store processes
   queue = []
   
   current_time = 0
   completed = 0
   
   # Loop until all processes are completed
   while completed < n:
       # Add arrived processes to the queue
       for i in processes:
           if arrival_time[i] <= current_time and i not in queue:
               queue.append(i)
       
       if not queue:
           current_time += 1
           continue
       
       # Execute each process in the queue for the time quantum
       for process in queue:
           if remaining_time[process] > time_quantum:
               starting_time[process] = current_time
               current_time += time_quantum
               remaining_time[process] -= time_quantum
           else:
               starting_time[process] = current_time
               current_time += remaining_time[process]
               remaining_time[process] = 0
               finishing_time[process] = current_time
               completed += 1
               queue.remove(process)

   return arrival_time,burst_time,priority,starting_time, finishing_time
        
         
      
