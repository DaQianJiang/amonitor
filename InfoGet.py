import os
import time
from ExcelOprate import excelOprate


class GetInfo(object):
    def __init__(self,counter):
        self.count = counter
        self.cpu_data = [["时间","CPU占用"]]
        self.mem_data = [["时间","内存占用"]]

    #获取cup信息,并返回
    def get_cpuinfo(self):
        #self.cpu_data = [["时间","CPU占用"]]
        #self.cpu_data=[]
        result = os.popen("adb shell dumpsys cpuinfo | findstr com.smzc.hci")
        cpuinfo = result.readline().split("%")[0].strip()
        currtent_time = self.get_currenttime()
        print("cpu:%s"%cpuinfo,"time:%s"%currtent_time)
        self.cpu_data.append([currtent_time,cpuinfo])
        #print(self.cpu_data)
        return self.cpu_data



    #获取当前时间
    def get_currenttime(self):
        #current_times = time.time()
        current_times = time.strftime("%H:%M:%S",time.localtime())
        return current_times

    #执行获取alldata列表
    def run(self,sleep_time):
        while self.count >0:
            self.get_cpuinfo()
            self.count-=1;
            time.sleep(sleep_time)
        cpu_data = monitor.get_cpuinfo()
        print(cpu_data)
        excelOprate().save_data("cpu占用",cpu_data)





if __name__ == '__main__':
    monitor = GetInfo(10)
    monitor.run(3)




