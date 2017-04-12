import collections
import struct
import functools
import define
import itertools


def __read_int_data(in_file):
    '''
    讀入binary file並切成數字list
    :param in_file: 
    :return: tid,data list
    '''
    rec = in_file.read(12)
    if not rec: return
    header = struct.unpack('3i', rec)
    size = header[-1]
    data = struct.unpack(str(size) + "i", in_file.read(4 * size))
    return header[0],data


def __read_tuple_data(in_file):
    '''
    讀入binary file並切成 tuple list
    :param in_file: 
    :return: tid,data list
    '''
    rec=in_file.read(12)
    if not rec:return
    header=struct.unpack('3i',rec)
    k=header[1]
    size=header[2]
    data=struct.unpack(str(size) + "i", in_file.read(4 * size))
    data_list=list(data[i:i+k] for i in range(0,size,k))
    return header[0],data_list


def __write_data(tid:int, new_candidate_itemset:list, k:int, out_f):
    chain_data=[c for c in itertools.chain(*new_candidate_itemset)]
    head=struct.pack("3i",tid,k,len(chain_data))
    data=struct.pack('%di'%len(chain_data),*chain_data)
    out_f.write(head+data)


def gen_large_itemset(large_itemset_counter:collections.Counter, sup: int) -> set:
    new_large_itemset={item for item, cnt in large_itemset_counter.items() if cnt >= sup}
    large_itemset_counter.clear()
    return new_large_itemset


def scandb_1st(work_path: str, input_file: str, counter: collections.Counter, sup: int) -> int:
    with open(work_path + input_file, 'rb', define.BUFFER_SIZE) as in_f:
        iter_read_data = iter(functools.partial(__read_int_data, in_f), None)
        input_line=0
        for tid,trans_rec in iter_read_data:
            input_line+=1
            counter.update(trans_rec)
    return input_line


def scandb_2nd(work_path: str, input_file: str, large_itemset: set, counter:collections.Counter, output_file: str) -> int:
    output_lines=0
    with open(work_path + input_file, 'rb',define.BUFFER_SIZE) as in_f, open(work_path + output_file, 'wb', define.BUFFER_SIZE) as out_f:
        iter_read_data = iter(functools.partial(__read_int_data, in_f), None) #建立一個讀檔的 iter 物件.
        for tid,trans_rec in iter_read_data:    #載入每一筆紀錄的TID及itemlist
            candidate_itemset=[item for item in trans_rec if item in large_itemset] #找出Candidate itemset
            new_candidate_itemset=list(itertools.combinations(candidate_itemset,2)) #組出所有的組合
            counter.update(new_candidate_itemset)   #計數
            __write_data(tid, new_candidate_itemset, 2, out_f)   #輸出至檔案中
            output_lines+=1
    return output_lines


def scandb_kth(work_path: str, input_file:str,k:int, large_itemset: set,large_itemset_counter:collections.Counter, output_file: str) -> int:
    output_lines = 0
    new_candidate_itemset=list()
    with open(work_path + input_file, 'rb') as in_f, open(work_path + output_file, 'wb') as out_f:
        iter_read_data=iter(functools.partial(__read_tuple_data,in_f),None) #建立一個讀檔的iter物件
        #讀入並處理每一筆交易紀錄
        for tid,trans_rec in iter_read_data:
            candidate_itemset=[item for item in trans_rec if item in large_itemset] #取得candidate itemset
            size=len(candidate_itemset)
            #產生candidate itemset
            for i in range(size-1):
                for j in range(i+1,size):
                    if candidate_itemset[i][:-1]!=candidate_itemset[j][:-1]:break
                    new_candidate_itemset.append(candidate_itemset[i]+(candidate_itemset[j][-1],))
            #計數
            large_itemset_counter.update(new_candidate_itemset)
            #若candidate itemset 數量大於1,下一次scandb時才會有新的candidate itemset
            if len(new_candidate_itemset)>1:
                __write_data(tid, new_candidate_itemset, k, out_f)
                output_lines += 1
            new_candidate_itemset.clear()

    return output_lines
