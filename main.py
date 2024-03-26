from fcfs import *
from SJF1 import *
from SJF2 import *
from R_R import *
from Priority import *
from tester import *



def edge_case_checker(opt,AT,BT,PR):
    if len(AT) != len(BT) or len(AT) != len(PR):
        return 0
    

def root(opt,AT=0,BT=0,PR=0):
    TAT = []
    WT = []
    result = edge_case_checker(opt,AT,BT,PR)
    if result:
        return -1
    
    # AT,BT,PR = splitter(AT,BT,PR)
    AT,BT,PR = convertor(AT,BT,PR)

    if opt == 'F.C.F.S':
        AT,BT,PR,ST,FT = FCFS(AT,BT,PR)

        
        
    elif opt == 'S.J.F':
        AT,BT,PR,ST,FT = sjf_non_preemptive(AT,BT,PR)

        
    elif opt == 'S.J.F-Pre':
        AT,BT,PR,ST,FT = sjf_preemptive(AT,BT,PR)

        
    elif opt == 'Priority':
        AT,BT,PR,ST,FT = priority_non_preemptive(AT,BT,PR)

        
    elif opt == 'Round-Robin':
        AT,BT,ST,PR,FT = round_robin(AT,BT,PR)

            
    TAT = cal_tat_list(AT,FT)
    WT  = cal_tat_list(BT,TAT)

    return AT,BT,PR,ST,FT,TAT,WT
