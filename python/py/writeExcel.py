#-*- coding:utf-8 -*-
from tempfile import TemporaryFile
from xlwt import Workbook

book = Workbook(encoding='utf-8')
sheet = book.add_sheet('order')

sheet.write(0,0, 'parent_id')
sheet.write(0,1, 'order_id')
sheet.write(0,2, 'seller_nick')
sheet.write(0,3, 'auction_title')

dataFile = open('d:/20120911')

line = dataFile.readline()
row = 1
while line != '':
    cols = line.split('\001')
    key = cols[0]
    if key == 'service_detail':
        sheet.write(row, 0, cols[1])
        sheet.write(row, 1, cols[2])
        sheet.write(row, 2, cols[4])
        sheet.write(row, 3, cols[6])
        row += 1
    line = dataFile.readline()

book.save('d:/dev/python/py/order.xls')
book.save(TemporaryFile())

