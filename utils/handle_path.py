#-*- coding: utf-8 -*-
#@Time    : 2022/10/21
#@Author  : xintian

import os
# print(__file__)#当前文件路径
# print(os.path.dirname(__file__))#上一级路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)#工程路径
#-----2、data路径--------------
data_path = os.path.join(project_path,'data')
#-----3、log路径--------------
log_path = os.path.join(project_path,'logs')
#-----4、配置路径--------------
config_path = os.path.join(project_path,'configs')
#-----5、报告路径--------------
report_path = os.path.join(project_path,'report\\tmp')

if __name__ == '__main__':
    print('工程路径>>> ',project_path)
    print('测试数据路径>>> ',data_path)
    print('log路径>>> ',log_path)
    print('报告路径>>> ',report_path)
    print('配置路径>>> ', config_path)


