import time
import struct


class RecordTime:
    """
    紀錄時間物件
    """
    process_start_time=0    #程序開始時間
    process_end_time=0      #程序結束時間
    task_start_time=0       #工作開始時間
    task_end_time=0         #工作結束時間
    task_name=''             #工作名稱
    step_start_time=0       #步驟開始時間
    step_end_time=0         #步驟結束時間
    step_name=''             #步驟名稱

    def proces_start(self):
        self.process_start_time=time.time()
        print("Process start.")
        print('-'*60)

    def process_end(self):
        self.process_end_time=time.time()
        print("Process end,spend time: ",self.process_end_time-self.process_start_time," sec")

    def task_start(self,taskName=''):
        self.task_name=taskName
        self.task_start_time=time.time()
        print("**",taskName," Task start.")

    def task_end(self):
        self.task_end_time=time.time()
        print("**",self.task_name," Task end,spend time:",self.task_end_time-self.task_start_time," sec")
        print('-'*60)

    def step_start(self,step_name=''):
        self.step_name=step_name
        self.step_start_time=time.time()
        print("\t\t",step_name,"\tstart.")

    def step_end(self):
        self.step_end_time=time.time()
        print("\t\t",self.step_name," \t end,spend time:",self.step_end_time-self.step_end_time," sec")
