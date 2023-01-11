from datetime import datetime
import re
fin = open('/Users/yangxiaotong/Desktop/95888_DFP/homework2/cme.20210709.c.pa2','rt',encoding = 'utf-8')
fout = open('/Users/yangxiaotong/Desktop/95888_DFP/homework2/CL_expirations_and_settlements.txt','wt',encoding='utf-8')


fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('Futures','Contract','Contract','Futures','Options','Options'))
fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('Code','Month','Type','Exp Date','Code','Exp Date'))
fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('-------','-------','-------','-------','-------','-------'))

list1 = []
for line in fin:
    if(line.startswith('B')):
        if((line[5]=='C' and line[6] == 'L' and line[7] == ' ') or (line[6]=='C' and line[7] == 'L') or (line[5]=='L' and line[6] == 'O' and line[7] == ' ') or (line[6]=='L' and line[7] == 'O')):
            list1.append(line.split())
n = len(list1)
list_fc_b1 = [] # future type for B
list_fc_b2 = [] # opt type for B
list_cm_b1 = []
list_cm_b2 = []
#list_ct=[]
list_fed = []
list_oc = []
list_oed = []
start_date = datetime.strptime('202109','%Y%m')
end_date = datetime.strptime('202312','%Y%m')
for i in range(n):
    dt = datetime.strptime(list1[i][2][3:9],'%Y%m')
    if dt <= end_date and dt >= start_date:
        if list1[i][2][0:3] == 'FUT':
            list_fc_b1.append(list1[i][1][-2:])
            cm = list1[i][2][3:7] + '-' + list1[i][2][7:9]
            list_cm_b1.append(cm)
            fed = re.findall(r'\d+',list1[i][3])[0][-8:-4]+'-'+re.findall(r'\d+',list1[i][3])[0][-4:-2] + '-' + re.findall(r'\d+',list1[i][3])[0][-2:]
            list_fed.append(fed)
        if list1[i][2][0:3] == 'OOF':
            cm = list1[i][2][3:7] + '-' + list1[i][2][7:9]
            list_cm_b2.append(cm)
            oed = re.findall(r'\d+', list1[i][4])[0][-8:-4] + '-' + re.findall(r'\d+', list1[i][4])[0][-4:-2] + '-' + \
                  re.findall(r'\d+', list1[i][4])[0][-2:]
            list_oed.append(oed)

for i in range(len(list_cm_b1)):
    list_fed[i]
    fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('CL', list_cm_b1[i], 'Fut', list_fed[i], '',
                                                        ''))
for i in range(len(list_cm_b2)):
    list_oed[i]
    fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('CL', list_cm_b2[i], 'Opt', '', 'LO',
                                                        list_oed[i]))
fin.close()

# tables for 81
fin = open('/Users/yangxiaotong/Desktop/95888_DFP/homework2/cme.20210709.c.pa2','rt',encoding = 'utf-8')
fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('Futures','Contract','Contract','Strike','Settlement'))
fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('Code','Month','Type','Price','Price'))
fout.write('{:12s}{:12s}{:12s}{:12s}{:12s}\n'.format('-------','-------','-------','-------','-------'))
list2 = []
for line in fin:
    if(line.startswith('81')):
        if((line[5]=='C' and line[6] == 'L' and line[7] == ' ') or (line[6]=='C' and line[7] == 'L') or (line[5]=='L' and line[6] == 'O' and line[7] == ' ') or (line[6]=='L' and line[7] == 'O')):
            list2.append(line.split())


n1 = len(list2)
list_fc_81 = [] # future type for B
list_fc_82 = [] # opt type for B
list_cm_81 = []
list_cm_82 = []
list_ct_8=[]
list_sp_81 = []
list_sp_82 = []
list_set_81 = []
list_set_82 = []
start_date = datetime.strptime('202109','%Y%m')
end_date = datetime.strptime('202312','%Y%m')

#print(date)
for i in range(n1):
    dt = datetime.strptime(list2[i][3][:6],'%Y%m')
    if dt <= end_date and dt >= start_date:
        if list2[i][2][0:3] == 'FUT':
            list_fc_81.append(list2[i][1][-2:])

            cm = list2[i][3][:4] + '-' + list2[i][3][4:6]
            list_cm_81.append(cm)
            #print(list_cm_81)
            set_p = re.findall(r'\d+',list2[i][4][61:])
            set_p = int(set_p[0]) / 100
            list_set_81.append(set_p)
            #print(set_p)
        if list2[i][2][0:3] == 'OOF':
            cm_82 = list2[i][3][:4] + '-' + list2[i][3][4:6]
            list_cm_82.append(cm_82)
            if list2[i][2][3] == 'C':
                list_ct_8.append('Call')
            if list2[i][2][3] == 'P':
                list_ct_8.append('Put')
            list_sp_82.append(int(list2[i][4][:7])/1000)
            set_p1 = re.findall(r'\d+', list2[i][4][61:])
            set_p1 = int(set_p1[0]) / 100
            list_set_82.append(set_p1)

for i in range(len(list_cm_81)):
    fout.write('{:12s}{:12s}{:12s}{:12s}{:12.2f}\n'.format('CL', list_cm_81[i], 'Fut', '',
                                                        list_set_81[i]))

for i in range(len(list_cm_82)):
     fout.write('{:12s}{:12s}{:12s}{:12.2f}{:12.2f}\n'.format('CL', list_cm_82[i], list_ct_8[i], list_sp_82[i],
                                                        list_set_82[i]))

fin.close()
fout.close()