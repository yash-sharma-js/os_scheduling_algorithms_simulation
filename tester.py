def convertor(AT,BT,PR):#CONVERTES INTO INT
    print("INSIDE CONVERTOR")
    AT = list(map(int,AT))
    BT = list(map(int,BT))
    PR = list(map(int,PR))
    print(AT,BT,PR)

    return AT,BT,PR


def sorting(AT,*BT,PR):   #SORT THE AT AND BT ACORDINGLY
    for X in range(len(AT)):
        for Y in range(len(AT)):
            if(AT[X]<AT[Y]):
                AT,BT,PR =swap(AT,BT,X,Y,PR)
    return AT,BT,PR            

def swap(AT,BT,X,*Y,PR):
    temp=AT[X]
    AT[X]=AT[Y]
    AT[Y]=temp

    temp=BT[X]
    BT[X]=BT[Y]
    BT[Y]=temp

    temp=PR[X]
    PR[X]=PR[Y]
    PR[Y]=temp
    return AT,BT,PR

def dummyval(AT,BT):
    DAT=[]
    DBT=[]
    for X in range(0,len(AT)):
        DAT.append(AT[X])
        DBT.append(BT[X])
    return DAT,DBT

def cal_tat_list(ST,FT):
    TAT = []
    for x in range(len(ST)):
        TAT.append((FT[x] - ST[x]))
    return TAT

def splitter(AT,BT,PR):
    AT = AT.split(',')
    BT = BT.split(',')
    PR = PR.split(',')
    return AT,BT,PR


def p_id_cal(AT):
    p_id = []
    for x in range(len(AT)):
        p_id.append('p{}'.format(x))
    return p_id    

    

