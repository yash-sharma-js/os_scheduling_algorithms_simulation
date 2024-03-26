# # import matplotlib.pyplot as plt
# # import numpy as np

# # def create_gantt_chart(tasks, start_times, durations):
# #     fig, ax = plt.subplots()

# #     yticks = np.arange(len(tasks))
# #     ax.set_yticks(yticks)
# #     ax.set_yticklabels(tasks)

# #     ax.grid(True)

# #     for i, task in enumerate(tasks):
# #         start = start_times[i]
# #         duration = durations[i]
# #         ax.barh(i, duration, left=start, height=0.5, align='center', edgecolor='black', label=task)
        
# #         # Add text inside the bar
# #         ax.text(start + duration / 2, i, f'{task} ({start}-{start + duration})', ha='center', va='center', color='white')

# #     ax.set_xlabel('Time')
# #     ax.set_ylabel('Tasks')
# #     ax.set_title('Gantt Chart')

# #     ax.invert_yaxis()  # Invert y-axis to have the tasks listed from top to bottom

# #     plt.show()

# # # Example data
# # tasks = ['Task 1', 'Task 2', 'Task 3','Tassk 4']
# # start_times = [1, 3, 6,9]  # Start times of tasks
# # durations = [2, 4, 3,80]    # Durations of tasks

# # create_gantt_chart(tasks, start_times, durations)



# # x = int(input("start :"))
# # y= int(input("Times :"))

# # for z in range(1,y):
# #     print("bet {}".format(x*2))
# #     x+=x*2
# #     print("AFTER {}".format(x))

    
# # print(x)    

# def sort(x):
#     x=5
#     y=6
#     h=[74,5,5,8,87,5]
#     if x:
#         y=9
#     return x,y,h
# def p(x):
#     x,y,h=sort(x)
#     print(x,y,h)
# p(7)    


# import matplotlib.pyplot as plt

# def draw_gantt_chart(processes, start_times, finish_times):
#     num_processes = len(processes)
#     fig, ax = plt.subplots()

#     # Set y-axis limits
#     ax.set_ylim(0, num_processes)

#     # Plotting the Gantt chart bars
#     for i in range(num_processes):
#         ax.barh(y=i, width=finish_times[i] - start_times[i], left=start_times[i], height=0.5, align='center', color='blue', alpha=0.6)
#         ax.text(start_times[i] + (finish_times[i] - start_times[i]) / 2, i, f'{processes[i]}', ha='center', va='center', color='white')

#     # Set axis labels and title
#     ax.set_xlabel('Time')
#     ax.set_ylabel('Process')
#     ax.set_title('Gantt Chart - FCFS')

#     # Set y-axis ticks and labels
#     ax.set_yticks(range(num_processes))
#     ax.set_yticklabels(processes)

#     # Remove grid lines
#     ax.grid(False)

#     # Show the plot
#     plt.show()

# # Example data (processes, starting times, finishing times)
# processes = ['P1', 'P2', 'P3', 'P4']
# start_times = [0, 3, 6, 8]
# finish_times = [5, 7, 10, 12]

# # Draw the Gantt chart
# draw_gantt_chart(processes, start_times, finish_times)




