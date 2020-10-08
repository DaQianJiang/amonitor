import xlwt
import xlrd
import os
import random
import time
import csv


ROOTPATH = os.path.abspath('.')
Excel_Path = os.path.join("monitor.xls")

class excelOprate(object):
    #将数据存入Excel中
    def save_data(self,sheet_name,value):
        #创建一个Excel对象
        excelfile = xlwt.Workbook()
        #创建一个sheet_name
        sheet = excelfile.add_sheet(sheet_name)
        nrows = len(value)#行
        ncols=len(value[0])#列
        for row in range(nrows):
            for col in range(ncols):
                sheet.write(row,col,value[row][col])
        excelfile.save(Excel_Path)
        print("excel 数据写入成功")

    def read_exceldata(self,sheet_name):
        file = xlrd.open_workbook(Excel_Path,sheet_name)
        table_data = file.sheet_by_name(sheet_name)
        return table_data

####CSV##########
    def write_data(self):
        while True:
            x = random.randint(0,100)
            y = random.randint(1,99)
            print((x,y))
            with open(os.path.join(ROOTPATH,'example.txt'),'a') as file:
                writer = csv.writer(file)
                writer.writerow((x,y))
            time.sleep(2)
    def read_csv(self):
        with open(os.path.join(ROOTPATH,'example.txt'),'r') as files:
            reader = csv.reader(files)
            for line in reader:
                print("oooo",line[0])
                print("iiii",line[1])


if __name__ == '__main__':
    ex = excelOprate()
    ta = ex.read_exceldata("cpu占用")
    for row in range(ta.nrows) :
        print(ta.cell(row,0).value)
        print(ta.cell(row,1).value)

    #ex.write_data()






