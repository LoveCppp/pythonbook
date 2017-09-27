#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xls.py.py
# @Author: For lg224@foxmail.com
# @Date  : 9/27/17

import xlsxwriter

workbook=xlsxwriter.Workbook("demo1.xlsx") #create excel file

worksheet=workbook.add_worksheet() #create work object

worksheet.set_column('A:A',20) #SET FIRST LIST WIDTH 20PX

bold=workbook.add_format({'bold':True}) #define add blod style

worksheet.write('A1','Hello')

worksheet.write('A2','World',bold)
worksheet.write('B2',u'zhongwencese',bold)


worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')
#worksheet.insert_image('B5','img/python-logo.png')
workbook.close()










