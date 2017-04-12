# Data mining home work 1:apriori Algorithm
import define as define
import functions as func
import module
import collections

large_itemset_counter=collections.Counter() #計數器
rectime = module.RecordTime()   #計算時間物件
rectime.proces_start()  #紀錄開始時間
k = 0   # scandb 次數
tot_cnt = 0 #large itemset 數量加總用變數

#顥示設定訊息
print("\tWork path=",define.WORK_PATH)
print("\tInput file=", define.INPUT_FILE)
print('\tmin sup=', define.MIN_SUP)

# Scandb first time 1111111111111111111111111111111111111111111111111111111111111111111111111111111
rectime.task_start(" 1st scan db")
k=1
input_file=define.INPUT_FILE
output_file=None

input_lines = func.scandb_1st(define.WORK_PATH, input_file, large_itemset_counter,define.MIN_SUP)

print('\t\tInput lines=', input_lines)

large_itemset=func.gen_large_itemset(large_itemset_counter,define.MIN_SUP)

#加總至 size of frq item
tot_cnt += len(large_itemset)
print("\t\tSize of %d-large itemset=%d" % (k, len(large_itemset)), "\tCrosssum of frq items=", tot_cnt)
rectime.task_end()  #第1次 scan db 結束

#   Scandb second time  2222222222222222222222222222222222222222222222222222222222222222222222222
rectime.task_start(' 2nd scan db')
k=2
input_file=define.INPUT_FILE
output_file="temp1.data"

output_lines = func.scandb_2nd(define.WORK_PATH,input_file,large_itemset,large_itemset_counter,output_file)

print('\t\tOutput lines=', output_lines)

large_itemset=func.gen_large_itemset(large_itemset_counter,define.MIN_SUP)

tot_cnt += len(large_itemset)
print("\t\tSize of %d-large itemset=%d" % (k, len(large_itemset)), "\tCrosssum of frq items=", tot_cnt)
rectime.task_end()

if len(large_itemset)==0:
    print('Tot frq item=', tot_cnt)
    rectime.process_end()
    exit()

# scan db k time 3333333333333333333333333333333333333333333333333333333333333333333333333333333
k = 3
input_file = "temp1.data"
output_file = "temp2.data"
while True:
    rectime.task_start(" %d-th scan db" % k)

    output_lines = func.scandb_kth(define.WORK_PATH,input_file,k,large_itemset,large_itemset_counter,output_file)

    print('\t\tOutput lines=', output_lines)

    large_itemset = func.gen_large_itemset(large_itemset_counter, define.MIN_SUP)

    tot_cnt += len(large_itemset)

    print("\t\tSize of %d-large itemset=%d"%(k,len(large_itemset)),"\tCrosssum of frq items=", tot_cnt)

    rectime.task_end()
    if len(large_itemset) == 0 or output_lines<define.MIN_SUP: break
    k += 1
    #將輸入檔和輸入檔對調
    input_file,output_file=output_file,input_file

print('Tot frq item=',tot_cnt)
rectime.process_end()
