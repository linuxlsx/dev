#-*- coding:utf-8 -*-

from xlrd import open_workbook

book = open_workbook('d:/dev/python/py/nongye_user.xls')

#get the first sheet
dataSheet = book.sheet_by_index(0)

rows = dataSheet.nrows

users = []
for row_index in range(rows):
    nick = dataSheet.cell(row_index, 0).value.strip()
    nickEncode = nick.encode('utf-8')
    userId = int(dataSheet.cell(row_index, 1).value)
    tmp = str(userId) + "," + nickEncode + "\n"
    users.append(tmp)

dataFile = open("d:/dev/python/py/nongye_user.txt", 'w')

for user in users:
    dataFile.write(user)

dataFile.close()
