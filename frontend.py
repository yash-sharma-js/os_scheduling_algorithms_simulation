import tkinter as tk
from tkinter import ttk
from tkinter import * 
from main import root
from structure_input import * 




def clear_screen(tree):
    tree.pack_forget()

def detailed_table(tree,p_id, AT, BT, PR, ST, FT):    # Adds Content to dummy table
    print(p_id, AT, BT, PR, ST, FT)
    tree.delete(*tree.get_children())

    for i, (pid, arrival_time, burst_time, priority, starting_time, finishing_time) in enumerate(zip(p_id, AT, BT, PR, ST, FT), start=1):
        tree.insert("", "end", text=str(i), values=(pid, arrival_time, burst_time, priority, starting_time, finishing_time))


def create_table(root):
    # Create a Frame to contain the Treeview widget with borders
    frame = ttk.Frame(root, borderwidth=2, relief="groove")
    # frame.configure()
    frame.pack(fill="both", expand=True)
    Label(frame,text="Detailed Table").pack()
    

    # Create a Treeview widget
    tree = ttk.Treeview(frame)

    # Define columns
    tree["columns"] = ("p_id", "arrival_time", "burst_time","Priority","StartingTime","FinishingTime")

    # Format columns̥
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
    tree.column("p_id", anchor=tk.W, width=100)
    tree.column("arrival_time", anchor=tk.CENTER, width=100)
    tree.column("burst_time", anchor=tk.CENTER, width=100)
    tree.column("Priority", anchor=tk.CENTER, width=100)
    tree.column("StartingTime", anchor=tk.CENTER, width=100)
    tree.column("FinishingTime", anchor=tk.CENTER, width=100)

    # Create headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("p_id", text="P_id", anchor=tk.W)
    tree.heading("arrival_time", text="Arival Time", anchor=tk.CENTER)
    tree.heading("burst_time", text="Burst Time", anchor=tk.CENTER)
    tree.heading("Priority", text="Priority", anchor=tk.CENTER)
    tree.heading("StartingTime", text="Starting Time", anchor=tk.CENTER)
    tree.heading("FinishingTime", text="Finishing Time", anchor=tk.CENTER)

    # Insert data into the table
    # data = [
    #     ("P1", 0, "10",0,20,20),
    #     ("P2", 1, "30",0,20,20),
    #     ("P3", 2, "50",0,20,20),
    #     ("P4", 3, "60",0,20,20),
    #     ("P5", 4, "20",0,20,20)
    # ]
    # for i, (p_id, arrival_time, burst_time,Priority,StartingTime,FinishingTime) in enumerate(data, start=1):
    #     tree.insert("", "end", text=str(i), values=(p_id, arrival_time, burst_time,Priority,StartingTime,FinishingTime))

    # Pack the Treeview widget
    tree.pack(expand=True, fill=tk.BOTH)
    return tree


def _table(root,x,y,TAT,WT,textA,textB):
    # Create the treeview widget
    table = ttk.Treeview(root, columns=(textA, textB), show='headings')
    table.configure(height=5)

    # Define column headings
    table.heading(textA, text=textA)
    table.heading(textB, text=textB)

    # Insert data into the table using loops
    for i, (starting_time, finishing_time) in enumerate(zip(x,y), start=1):
        table.insert("", "end", text=str(i), values=( starting_time, finishing_time))#

    # Set column widths
    table.column(textA, width=150)
    table.column(textB, width=150)

    # Pack the table into the root window

    Label(app,text="Avg. T.A.T = (F.T - A.T)/N",bg='#ADD8E6',font=("Helvetica", 17)).place(x=260,y=430)
    Label(app,text="∴ Avg. T.A.T = {}".format(round(sum(TAT)/len(TAT),3)),bg='#ADD8E6',font=("Helvetica", 17)).place(x=260,y=480)
    
    Label(app,text="Avg. W.T = (B.T - T.A.T)/N",bg='#ADD8E6',font=("Helvetica", 17)).place(x=550,y=430)
    Label(app,text="∴ Avg. W.T = {}".format(sum(WT)/len(WT)),bg='#ADD8E6',font=("Helvetica", 17)).place(x=550,y=480)


    table.pack()
   
# def cal_tat_wt(rframe):                                               # Bottom right frame
#     _table(rframe)
#     pass



def get_values(tree):
    AT = (temp_at.get()).split(',')
    BT = (temp_bt.get()).split(',')
    PR = (temp_pri.get()).split(',')
    print(AT,BT,PR)
    print("{} SELECTED".format(selected_option.get()))
    opt= selected_option.get()
    COMBINED_AT_BT_PR_ST_FT_TAT_WT = root(opt,AT,BT,PR)
    if(COMBINED_AT_BT_PR_ST_FT_TAT_WT == -1):
        print("SHOW ERRROR")
        return
    AT,BT,PR,ST,FT,TAT,WT = COMBINED_AT_BT_PR_ST_FT_TAT_WT
    p_id = p_id_cal(AT)
    detailed_table(tree,p_id,AT,BT,PR,ST,FT)
    _table(blframe,ST,FT,TAT,WT,textA="S.T",textB="F,T")
    _table(brframe,BT,TAT,TAT,WT,textA="BT",textB="TAT")



#                                           -- FRONTEND PART STARTS HERE
app = tk.Tk()

app.title("OS SIMULATOR")
XX=855
YY=520
bgg = "#8AC7DB"
fgg='black'

app.geometry("855x550")
app.resizable(0,0)
# app.minsize(635,455)
# app.maxsize(733,434)
app.configure(bg='#ADD8E6')

#   pack has attributes ancher takes : dir ;- south esst -- se ,,, ,, ,, etc
lframe = Frame(app,bg=bgg,width=250,height=455,bd=1 ,padx=10,pady=10)
lframe.pack(side=LEFT,fill=Y)

rframe = Frame(app,height=455,bg="#ADD8E6")
rframe.pack(fill=X)



Label(lframe,bg=bgg,text="Arival Time :",fg=fgg,width=20,height=2,font=("Helvetica", 15)).grid(row=0,column=0)
temp_at = Entry(lframe,width=20,font=("Helvetica", 12))
temp_at.grid(row=1,column=0,pady=8)

Label(lframe,bg=bgg,text="Priority :",fg=fgg,width=20,height=2,font=("Helvetica", 15)).grid(row=2,column=0)
temp_pri = Entry(lframe,width=20,font=("Helvetica", 12))
temp_pri.grid(row=3,column=0,pady=8)

Label(lframe,bg=bgg,text="Burst Time :",fg=fgg,width=20,height=2,font=("Helvetica", 15)).grid(row=4,column=0)
temp_bt = Entry(lframe,width=20,font=("Helvetica", 13))
temp_bt.grid(row=5,column=0,pady=8)

tree = create_table(rframe) #to create table


#-- CREATE OPTION FIELD
Label(lframe,bg=bgg,text="Schedule By :",fg=fgg,font=("Helvetica", 15)).grid(row=6,column=0,pady=10)
options = ["F.C.F.S", "S.J.F", "S.J.F-Pre", "Priority", "Priority-pre", "Round-Robin"]
# Variable to store the selected option
selected_option = tk.StringVar(lframe)
selected_option.set(options[0])  # Set default option
# Dropdown menu
dropdown = tk.OptionMenu(lframe,selected_option, *options)
dropdown.configure(width=20,font=15)
dropdown.grid(row=7,column=0,pady=5)


Button(lframe,bg='#FFFFFF',width=15,fg=fgg,text="START",pady=10,command=lambda:get_values(tree),font=15).grid(row=8,column=0,pady=15)
Button(lframe,text="Clear",bg='black',fg='white',width=15,pady=10,font=15).grid(row=9,column=0,pady=15)




blframe = Frame(rframe,bg='#ADD8E6',width=200,height=800)         #left frame 
blframe.pack(side=LEFT,fill=BOTH,expand=True) 

head = Label(blframe,text="Avg T.A.T time ")
head.pack(side="top", fill="both", expand=True)


brframe = Frame(rframe,bg='#ADD8E6' ,width=200,height=800)        # Right Frame 
brframe.pack(side=LEFT ,fill=BOTH,expand=True) 

head1 = Label(brframe,text="Avg Waiting time ")
head1.pack(side="top", fill="both", expand=True)
# cal_tat_wt(rframe) #to calculate tat and wt


app.mainloop()