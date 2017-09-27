#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xls2.py.py
# @Author: For lg224@foxmail.com
# @Date  : 9/27/17

import xlsxwriter

workbook=xlsxwriter.Workbook("chart.xlsx") #create excel file

worksheet=workbook.add_worksheet() #create work object

chart=workbook.add_chart({'type':'column'})

title=[u'name','Monday','Tuesday','Wednesday','Thursday','Firday','staturday','Sunday','Average']

buname=['index','newscenter','shop','play','baby']

data=[
    [150,152,153,156,162,121,122],
    [20,31,89,95,100,99,122],
    [83,88,199,156,162,174,122],
    [201,202,197,156,162,175,122],
    [75,77,78,78,74,70,79],
]


format_title=workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()

format_ave=workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format("0.00")


worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)


def chart_series(cur_row):
    worksheet.write_formula('I'+cur_row,'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)
    chart.add_series(
        {
            'categories': '=Sheet1!$B$1:$H$1',
            'values': '=Sheet1!$B$'+cur_row+':$H$'+cur_row,
            'line':{'color':'black'},
            'name': '=Sheet1$A$'+cur_row,
        }
    )

for row in range(2,7):
    chart_series(str(row))


chart.set_size({'width':577,'height':287})
chart.set_title({'name':'week repart'})
chart.set_y_axis({'name':'Mb/s'})




worksheet.insert_chart('A8',chart)

workbook.close()
