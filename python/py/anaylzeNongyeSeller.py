#-*- coding:utf-8 -*-

from xlrd import open_workbook

class SellerTrade:
   
    def setNick(self, nick):
        self.nick = nick

    def getNick(self):
        return self.nick

    def setUserId(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def setGmvFee(self, gmvFee):
        self.gmvFee = gmvFee

    def getGmvFee(self):
        return self.gmvFee

    def setGmvUv(self, gmtUv):
        self.gmtUv = gmtUv

    def getGmvUv(self):
        return self.gmtUv

    def setAlipayFee(self, alipayFee):
        self.alipayFee = alipayFee

    def getAlipayFee(self):
        return self.alipayFee

    def setAlipayUv(self, alipayUv):
        self.alipayUv = alipayUv

    def getAlipayUv(self):
        return self.alipayUv


		
book = open_workbook('d:/dev/python/py/nongye_alipay.xls')
dataSheet = book.sheet_by_index(0)
sellerTradeDict = {}
rows = dataSheet.nrows
for row_index in range(1, rows):
    st = SellerTrade()
    pt = str(int(dataSheet.cell(row_index, 0).value))
    
    st.setNick(dataSheet.cell(row_index, 1).value.strip().encode('utf-8'))
    st.setUserId(str(int(dataSheet.cell(row_index, 2).value)))
    st.setGmvFee(int(dataSheet.cell(row_index, 3).value))
    st.setGmvUv(int(dataSheet.cell(row_index, 4).value))
    st.setAlipayFee(int(dataSheet.cell(row_index, 5).value))
    st.setAlipayUv(int(dataSheet.cell(row_index, 6).value))

    ptList = sellerTradeDict.get(pt, None)
    if ptList == None:
        ptList = []
        ptList.append(st)
        sellerTradeDict[pt] = ptList
    else:
        ptList.append(st)


keys = sellerTradeDict.keys()
for key in keys:   
    fileKey = open('d:/dev/python/py/data/' + key, 'w')
    ptList = sellerTradeDict.get(key)
    for st in ptList:
        fileKey.write('%s\001%s\001%d\001%d\001%d\001%d\n' % (st.getNick(),st.getUserId(), st.getGmvFee(), st.getGmvUv(), st.getAlipayFee(), st.getAlipayUv()))
    
    fileKey.close()

