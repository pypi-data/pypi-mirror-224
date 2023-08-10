# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:32:55 2022

@author: Cheryl.fan
"""

import json
import inspect
import datetime
from .ObjJsonEncoding import *
from .EasyPyenum import *

class ReplyPy(object):
    systemCode="EasyPy" #系統代碼
    className="ReplyPy" #型別名稱 
    xReply=None #回報   
    functionCode=None #回覆功能
    repTime=None #收到回報的時間
    def __init__(self, dataStr):
        """
        Parameters
        ----------
        dataStr : json string
            前端回傳值.
        Returns
        -------
        None.
        """
        data=json.loads(dataStr)
        self.repTime=datetime.dateime.now().strftime("%Y%m%d %H:%M:%S")  
        self.functionCode=FunctionCode(data['functionCode'])          
        if MarketCode(data['marketType']) == MarketCode.Stocks:
            if GroupCode(data['groupCode']) == GroupCode.回覆:
                self.xReply=StockResponse(**data)
            else:
                self.xReply=StockReport(**data)
            
    '''
    def __init__(self, marketType, serialId, account, orderTime, orderDate, sessionType, orderType, closed, sideType, symbol, qty, price, priceType,\
                 priceBefore, priceAfter, orderNo, qtyCurrent, qtyNext, qtyDeal, confirmTime, code, codeMsg, canCancel, canModify, source, isPreOrder,\
                 avgPrice, updateTime, state, stateMsg, groupCode, opCode, branchId, salesCode, dataSrc, dealNo, settleType, brokerId, prgmType,\
                 prgmINSQ, subAccount, subDealNo, dealFlag):
        self.marketType=MarketType(marketType)
 
        if self.marketType == MarketType.Stocks:
            self._xReply = StockReply(serialId, account, orderTime, orderDate, sessionType, orderType, closed, sideType, symbol, qty, price, priceType,\
                                      priceBefore, priceAfter, orderNo, qtyCurrent, qtyNext, qtyDeal, confirmTime, code, codeMsg, canCancel, canModify,\
                                      source, isPreOrder, avgPrice, updateTime, state, stateMsg, groupCode, opCode, branchId, salesCode, dataSrc, dealNo,\
                                      settleType, brokerId, prgmType, prgmINSQ, subAccount, subDealNo, dealFlag)     
    '''
    
    '''
    JSON Format
    將TradePy轉換為Json格式再進行資料交換
    '''
    def jsonFormat(self, isNewLine: bool=False):
        """
        Parameters
        ----------
        isNewLine : bool, optional
            是否換行. The default is False.
        Returns
        -------
        json string
            JSON格式.
        """
        if isNewLine == True:
            return json.dumps(self, cls=ObjJsonEncoding,sort_keys=True, indent=4, ensure_ascii=False) # 換行
        else:
            return json.dumps(self, cls=ObjJsonEncoding, ensure_ascii=False) #不換行
    
'''
stock
'''
class StockReply(object):
    marketCode=None #市場別
    groupCode=None #回報型別
    account="" #帳號(前面包含 FBID + BID)       
    seqNo="" #網路單流水號   
    orderTime="" #委託時間
    orderDate="" #交易日
    sessionCode=None #盤別 {0:普通│ 1:零股│ 2:盤後│ 7:盤中零股}
    orderCode=None #交易別 {0:現股│ 1:融資│ 2:融券│ 22:先賣}
    side=None #買賣別 {B:買│ S:賣}
    symbol="" #標的代碼
    price=0 #委託價格 (原始)
    priceCode=None #價位別 {0:限價│ 4:市價}
    orderNo="" #委託書號
    qtyCurrent=0 #委託張/股數 (改量前)
    qtyNext=0 #委託張/股數 (改量後)
    code="" #錯誤代碼
    source="" #來源別: “電子單” / “現場單” / …    
    def __init__(self, marketCode, groupCode, seqNo, account, orderTime, orderDate, sessionCode, orderCode, side, symbol, price, priceCode,\
                 orderNo, qtyCurrent, qtyNext, code, source):
        """
        Parameters
        ----------
        marketCode : Enum
            市場別<Stocks=0>.
            #SubBorkerages=1
            #Futures=2
            #OverseasFurutes=3
            #Foreigns=4
        groupCode : Enum
            回報型別<回覆="00",委託="03",成交="04">.
        seqNo : string
            網路序號.
        account : string
            帳號.
        orderTime : string
            委託時間.
        orderDate : string
            委託日期.
        sessionCode : Enum
            盤別<普通=0,零股=1,盤後定盤=2,盤中零股=3>.
        orderCode : Enum
            委託別<現股=0,融資=1,融券=2,先賣沖=3>.
            #代辦融資=4
            #代辦融券=5
        side : Enum
            買賣別<Buy=0,Sell=1>.
        symbol : string
            標的代碼.        
        price : decimal
            委託價.
        priceCode : Enum
            價格別<限價=0,市價=1>.
            #平盤=2
            #跌停=3
            #漲停=4    
            #範圍市價=5       
        orderNo : string
            委託書號.
        qtyCurrent : integer
            改量前委託量.
        qtyNext : integer
            改量後委託量.        
        code : string
            錯誤代碼.
        source : string
            來源別.
        Returns
        -------
        None.
        """
        self.marketCode=MarketCode(marketCode)
        self.seqNo=seqNo
        self.account=account
        self.orderTime=orderTime
        self.orderDate=orderDate
        self.sessionCode=SessionCode(sessionCode)
        self.orderCode=OrderCode(orderCode)
        self.side=SideCode(side)
        self.symbol=symbol
        self.price=price
        self.priceCode=PriceCode(priceCode)
        self.orderNo=orderNo
        self.qtyCurrent=qtyCurrent
        self.qtyNext=qtyNext
        self.code=code
        self.source=source      
        self.groupCode=GroupCode(groupCode)       
    
'''
stock Response
第一式回報
'''
class StockResponse(StockReply):       
    qtyDeal=0 #成交數量
    confirmTime="" #回報時間
    closed="" #是否收盤 { Y:是 │ N:否}  
    qty=0 #委託張/股數 (原始)  
    priceBefore=0 #委託價格 (改價前)
    priceAfter=0 #委託價格 (改價後)    
    codeMsg="" #錯誤訊息
    canCancel="" #可否刪單 { Y:是 │ N:否}
    canModify="" #可否改量 { Y:是 │ N:否}   
    isPreOrder="" #預約單{ Y:是 │ N:否(盤中單)}
    avgPrice=0 #成交均價
    updateTime="" #異動時間
    state=None #委託單狀態碼
    stateMsg="" #委託單狀態       
    def __init__(self, marketCode, groupCode, seqNo, account, orderTime, orderDate, sessionCode, orderCode, side, symbol, price, priceCode,\
                 orderNo, qtyCurrent, qtyNext, code, source, qtyDeal, confirmTime, closed, qty, priceBefore, priceAfter, codeMsg, canCancel,\
                 canModify, isPreOrder, avgPrice, updateTime, state, stateMsg):
        """
        Parameters
        ----------
        qtyDeal : integer
            成交量.
        confirmTime : string
           回報時間.
        closed : string
            是否收盤. 
        qty : integer
            委託量.
        priceBefore : decimal
            改價前委託價.
        priceAfter : decimal
            改價後委託價.
        codeMsg : string
            錯誤訊息.
        canCancel : string
            可否刪單.
        canModify : string
            可否改量.        
        isPreOrder : string
            是否為預約單.
        avgPrice : decimal
            成交均價.
        updateTime : string
            異動時間.
        state : Enum
            委託單狀態<收到='0',交易所回覆失敗='9',成功='10',改量='20',刪單='30',全部成交='50',委託失敗='90'>.
        stateMsg : string
            委託單狀態訊息.
        Returns
        -------
        None.
        """
        super(StockResponse, self).__init__(marketCode, groupCode, seqNo, account, orderTime, orderDate, sessionCode, orderCode, side, symbol,\
                                            price, priceCode, orderNo, qtyCurrent, qtyNext, code, source)   
        self.qtyDeal=qtyDeal
        self.confirmTime=confirmTime
        self.closed=closed        
        self.qty=qty        
        self.priceBefore=priceBefore
        self.priceAfter=priceAfter
        self.codeMsg=codeMsg
        self.canCancel=canCancel
        self.canModify=canModify
        self.isPreOrder=isPreOrder
        self.avgPrice=avgPrice
        self.updateTime=updateTime
        self.state=OrderState(state)
        self.stateMsg=stateMsg

'''
stock Report
第二式回報
'''
class StockReport(StockReply):
    opCode=None #作業代碼
    branchId="" #分公司代碼
    sales="" #營業員
    dealNo="" #成交序號
    settleCode=None #交割型別
    brokerId="" #推薦券商代號
    prgmCode=None #智慧下單類型
    prgmINSQ="" #智慧下單網路序號
    subAccount="" #子帳
    subDealNo="" #子帳號成交序號
    dealFlag="" #成交回報旗標
    def __init__(self, marketType, groupCode, seqNo, account, orderTime, orderDate, sessionCode, orderCode, side, symbol, price, priceCode,\
                 orderNo, qtyCurrent, qtyNext, code, source, opCode, branchId, sales, dealNo, settleType, brokerId, prgmType, prgmINSQ,\
                 subAccount, subDealNo, dealFlag):
        """
        Parameters
        ----------
        opCode : Enum
            作業型別<預約失敗="02",委託成功="11",委託失敗="12",刪單成功="21",刪單失敗="22",改量成功="31",改量失敗="32",成交="40">.
        branchId : string
            分公司代碼.
        sales : string
            營業員
        dealNo : string
            成交序號.
        settleCode : Enum
            交割別<餘客交割=0,逐筆交割=1>.
        brokerId : string
            推薦券商.
        prgmCode : Enum
            智慧下單類型<通知=1,一般單回報=2,智慧單回報=3>.
        prgmINSQ : string
            智慧下單網路序號.
        subAccount : string
            子帳.
        subDealNo : string
            子帳號成交序號.
        dealFlag : Enum
            成交回報旗標<依據盤別=0,皆為股數=1>.
        Returns
        -------
        None.        
        """
        super(StockReport, self).__init__(marketType, groupCode, seqNo, account, orderTime, orderDate, sessionType, orderType, side, symbol,\
                                          price, priceCode, orderNo, qtyCurrent, qtyNext, code, source)
        self.opCode=OperationCode(opCode)
        self.branchId=branchId
        self.sales=sales
        self.dealNo=dealNo
        self.settleCode=SettleCode(settleCode)
        self.brokerId=brokerId
        self.prgmCode=ProgramCode(prgmCode)
        self.prgmINSQ=prgmINSQ
        self.subAccount=subAccount
        self.subDealNo=subDealNo
        self.dealFlag=DealFlagCode(dealFlag)
        