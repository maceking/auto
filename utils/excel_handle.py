#-*- coding: utf-8 -*-
#@Time    : 2022/10/21 20:35
#@Author  : mace
import xlrd
import json,sys
sys.path.append('.')
from utils.handle_path import data_path
#--------------判断是否是json------------------
def is_josn(inStr):
    try:
        json.loads(inStr)
    except:#只有try报错才执行里面的代码
        return False
    return True




def get_excel_data(sheetName,caseName,*colName,excelDir=data_path+r'/Delivery_System_V1.5.xls',selectCase):
    resList = []
    #1- 加载excel
    #formatting_info = True   保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #2- 获取对应具体的一个表
    workSheet = workBook.sheet_by_name(sheetName)

    # 把函数调用者的输入的列名--转化---列编号
    #----------------------------------------------------
    colIndxList = []#函数调用者输入列名，转化后的列编号--列表类型
    for i in colName:#遍历用户输入的列名--colName元组
        colIndxList.append(workSheet.row_values(0).index(i))
    print(colIndxList)
    #----------------------------------------------------

    #-----------------------挑选用例执行---------------------------
    selectList = []#挑选出来的用例
    if 'all' in selectCase:#全部执行这个接口的所有用例
        selectList = workSheet.col_values(0)
    else:#1- 某一个   2- 某一段  ['001','003-006']
        for one in selectCase:
            if '-' in one:#是一段用例
                start,end = one.split('-')# 3,6
                for i in range(int(start),int(end)+1):#(3,7)---3,4,5,6
                    selectList.append(caseName+f'{i:0>3}')#Login3---Login003
            else:
                selectList.append(caseName+f'{one:0>3}')
    #-------------------------------------------------------
    idx = 0#代表行号的初始值
    for one in workSheet.col_values(0):#获取第0列数据
        if caseName in one and one in selectList:
            #条件满足，这一行数据的对应列是需要的数据
            getColData = []#存放一行对应的很多列的数据
            for colIdx in colIndxList:
                res = workSheet.cell_value(idx,colIdx)#读取某一个单元格数据
                if is_josn(res):#判断单元格数据是否是json
                    res = json.loads(res)#转化--字典
                getColData.append(res)
            resList.append(getColData)
        idx += 1
    return resList



if __name__ == '__main__':#ctrl+j 快捷键
    configData = ['用例编号','标题','URL','请求参数']
    print(data_path)
    res = get_excel_data('登录模块','Login',*configData,selectCase=['001','003','006','all'])
    #print(res)
    for one in res:
        print(one)




