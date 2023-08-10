# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:32:28 2022

@author: Cheryl.fan
"""

import json
import inspect
import datetime
import logging.config
import os
from .ObjJsonEncoding import *
from .EasyPyenum import *
#from .SendMsg import *

logconf_file = os.path.join(os.path.dirname(__file__), 'easypy.config')
logging.config.fileConfig(logconf_file)
logger = logging.getLogger('MainLogger')        
filehandler = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.date.today()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
filehandler.setFormatter(formatter)        
logger.addHandler(filehandler)

class QueryPy(object):     
    systemCode="EasyPy" #系統代碼
    className="QueryPy" #型別名稱 
    queryCode=None #查詢別
    marketCode=None #市場
    account="" #帳號
    xQuery=None #x查詢
    def __init__(self, address: str="127.0.0.1"):
        pass
        '''        
        Parameters
        ----------
        address : string, optional
            Server IP address. The default is "127.0.0.1".         
        '''    
    
    def queryItem(self, send, account, queryCode: QueryCode=1, dtKindCode: DtKindCode=1, reportCode: ReportCode=0,\
                 marketCode: MarketCode=0, sessionCode: SessionCode=0):
        '''        
        Parameters
        ----------
        account : TYPE
            帳號.
        queryCode : QueryCode Enum, optional
            查詢別<交易日=0,庫存=1,成交單=2,委託單=3,權益數=4>. The default is 1.        
        dtKindCode : DtKindCode Enum, optional
            交易日型態<證券=1,期權=2>. The default is 0.
        reportCode : ReportCode Enum, optional
            回報型態<全部=0,上市櫃=1>. The default is 0.
        marketCode : MarketCode Enum, optional
            市場型別<Stocks=0,SubBorkerages=1,Futures=2,OverseasFurutes=3,Foreigns=4>. The default is 0.
        sessionCode : SessionCode Enum, optional
            盤別<普通=0,零股=1,盤後定盤=2,盤中零股=3>. The default is 0.
        Returns
        -------
        None.
        '''       
        self.queryCode=QueryCode(queryCode)
        self.marketCode=MarketCode(marketCode)
        self.account=account
        if self.marketCode == MarketCode.Stocks:
            self.xQuery=StockQuery(sessionCode, dtKindCode, reportCode)      
        self.__sendQuery(send, self.jsonFormat())
        
    '''
    
    '''
    def __sendQuery(self, send, jsonStr):
        """
        Parameters
        ----------
        jsonStr : string
            trade message(json format).
        Returns
        -------
        None.
        """
        send.msgTo(jsonStr)
        logger.info(jsonStr)
        pass
    
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
stock query
'''
class StockQuery:
    dtKindCode=None #查詢交易日別
    sessionCode=None #盤別
    reportCode=None #查詢回報別
    queryTime=None #查詢時間
    def __init__(self, sessionCode, dtKindCode, reportCode):
        """
        Parameters
        ----------
        sessionCode : Enum
            盤別<普通=0,零股=1,盤後定盤=2,盤中零股=3>..
        dtKindCode : Enum
            交易日型態<證券=1,期權=2>.
        reportCode : Enum
            回報型態<全部=0,上市櫃=1>.

        Returns
        -------
        None.
        """
        self.queryTime=datetime.datetime.now().strftime("%Y%m%d %H:%M:%S") 
        self.sessionCode=SessionCode(sessionCode)
        self.dtKindCode=DtKindCode(dtKindCode)
        self.reportCode=ReportCode(reportCode)



'''
query response
'''
class QueryResponse(object):
    xResponse=None #回覆
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
        queryCode=QueryCode(data['queryCode'])  
        if MarketCode(data['marketCode']) == MarketCode.Stocks:
            if queryCode == QueryCode.交易日:
                self.xResponse=self.TradeDate(**data)
            elif queryCode == QueryCode.庫存:
                self.xResponse=self.Inventory(**data)
            elif queryCode == QueryCode.成交單:
                self.xResponse=self.Execute(**data)
            else:#委託單
                self.xResponse=self.Request(**data)
                
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
    查詢交易日回覆
    '''
    class TradeDate(object):
        tradeDate=""
        sessionCode=None
        lastDate=""
        nextDate=""
        tradeTime=""
        haltTime=""
        state=None
        nextState=None
        nextChgTime=""
        dtKindCode=None
        def __init__(self, tradeDate, sessionCode, lastDate, nextDate, tradeTime, haltTime, state, nextState, nextChgTime, dtKindCode):
            """
            Parameters
            ----------
            tradeDate : string
                交易日.
            sessionCode : Enum
                盤別<普通=0,零股=1,盤後定盤=2,盤中零股=3>.
            lastDate : string
                最近交易日.
            nextDate : string
                次一交易日.
            tradeTime : string
                盤中交易時間.
            haltTime : string
                暫停交易時間.
            state : Enum
                目前狀態<盤中=0,預約=1,暫停=2>.
            nextState : Enum
                下次狀態<盤中=0,預約=1,暫停=2>.
            nextChgTime : string
                下次更改時間.
            dtKindCode : Enum
                交易日型態<證券=1,期權=2>.

            Returns
            -------
            None.
            """
            self.tradeDate=tradeDate
            self.sessionCode=sessionCode
            self.lastDate=lastDate
            self.nextDate=nextDate
            self.tradeTime=tradeTime
            self.haltTime=haltTime
            self.state=StateCode(state)
            self.nextState=StateCode(nextState)
            self.nextChgTime=nextChgTime
            self.dtKindCode=dtKindCode
        
    '''
    查詢庫存回覆
    '''
    class Inventory(object):
        symbol=""
        symbolName=""
        sessionCode=None
        qty0Info1=0
        qty0Info2=0
        qty0Info3=0
        qty0Info4=0
        qty0Info5=0
        qty1Info1=0
        qty1Info2=0
        qty1Info3=0
        qty1Info4=0
        qty1Info5=0
        qty2Info1=0
        qty2Info2=0
        qty2Info3=0
        qty2Info4=0
        qty2Info5=0
        qty3Info1=0
        qty3Info2=0
        qty3Info3=0
        qty3Info4=0
        qty3Info5=0
        cost=0
        exchange=""
        currency=""
        def __init__(self, symbol, symbolName, sessionCode, qty0Info1, qty0Info2, qty0Info3, qty0Info4, qty0Info5, qty1Info1, qty1Info2, qty1Info3,\
                     qty1Info4, qty1Info5, qty2Info1, qty2Info2, qty2Info3, qty2Info4, qty2Info5, qty3Info1, qty3Info2, qty3Info3, qty3Info4,\
                     qty3Info5, cost, exchange, currency):
            """
            Parameters
            ----------
            symbol : string
                標的代碼.
            symbolName : string
                標的名稱.
            sessionCode : Enum
                盤別<普通=0,零股=1,盤後定盤=2,盤中零股=3>.
            qty0Info1 : integer
                集保/興櫃昨日庫存(股數).
            qty0Info2 : integer
                集保/興櫃今日委託買進.
            qty0Info3 : integer
                集保/興櫃今日委託賣出.
            qty0Info4 : integer
                集保/興櫃今日成交買進.
            qty0Info5 : integer
                集保/興櫃今日成交賣出.
            qty1Info1 : integer
                融資昨日庫存(股數).
            qty1Info2 : integer
                融資今日委託買進.
            qty1Info3 : integer
                融資今日委託賣出.
            qty1Info4 : integer
                融資今日成交買進.
            qty1Info5 : integer
                融資今日成交賣出.
            qty2Info1 : integer
                融券昨日庫存(股數).
            qty2Info2 : integer
                融券今日委託買進.
            qty2Info3 : integer
                融券今日委託賣出.
            qty2Info4 : integer
                融券今日成交買進.
            qty2Info5 : integer
                融券今日成交賣出.
            qty3Info1 : integer
                零股昨日庫存(股數).
            qty3Info2 : integer
                零股今日委託買進.
            qty3Info3 : integer
                零股今日委託賣出.
            qty3Info4 : integer
                零股今日成交買進.
            qty3Info5 : integer
                零股今日成交賣出.
            cost : TYPE
                成本.
            exchange : string
                交易所.
            currency : string
                幣別.

            Returns
            -------
            None.
            """
            self.symbol=symbol
            self.symbolName=symbolName
            self.sessionCode=SessionCode(sessionCode)
            self.qty0Info1=qty0Info1
            self.qty0Info2=qty0Info2
            self.qty0Info3=qty0Info3
            self.qty0Info4=qty0Info4
            self.qty0Info5=qty0Info5
            self.qty1Info1=qty1Info1
            self.qty1Info2=qty1Info2
            self.qty1Info3=qty1Info3
            self.qty1Info4=qty1Info4
            self.qty1Info5=qty1Info5
            self.qty2Info1=qty2Info1
            self.qty2Info2=qty2Info2
            self.qty2Info3=qty2Info3
            self.qty2Info4=qty2Info4
            self.qty2Info5=qty2Info5
            self.qty3Info1=qty3Info1
            self.qty3Info2=qty3Info2
            self.qty3Info3=qty3Info3
            self.qty3Info4=qty3Info4
            self.qty3Info5=qty3Info5
            self.cost=cost
            self.exchange=exchange
            self.currency=currency
        
    '''
    查詢成交單回覆
    '''
    class Execute(object):
        dealNo=""
        seqNo=""
        orderDate=""
        orderNo=""
        account=""
        orderTime=""
        sessionCode=None
        orderCode=None
        side=None
        symbol=""
        price=0
        qtyDeal=0
        dealTime=""
        fee=0
        tax=0
        currency=""        
        def __init__(self, dealNo, seqNo, orderDate, orderNo, account, orderTime, sessionCode, orderCode, side, symbol, price, dealQty, dealTime,\
                     fee, tax, currency):
            """
            Parameters
            ----------
            dealNo : string
                成交序號.
            seqNo : string
                網路委託序號.
            orderDate : string
                委託日期.
            orderNo : string
                委託書號.
            account : string
                帳號.
            orderTime : string
                委託時間.
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
                成交價.
            dealQty : integer
                成交量.
            dealTime : string
                成交時間.
            fee : decimal
                手續費.
            tax : decimal
                交易稅.
            currency : string
                幣別.

            Returns
            -------
            None.
            """
            self.dealNo=dealNo
            self.seqNo=seqNo
            self.orderDate=orderDate
            self.orderNo=orderNo
            self.account=account
            self.orderTime=orderTime
            self.sessionCode=SessionCode(sessionCode)
            self.orderCode=OrderCode(orderCode)
            self.side=SideCode(side)
            self.symbol=symbol
            self.price=price
            self.dealQty=dealQty
            self.dealTime=dealTime
            self.fee=fee
            self.tax=tax
            self.currency=currency          
        
    '''
    查詢委託單回覆
    '''
    class Request(object):
        seqNo=""
        account=""
        orderTime=""
        orderDate=""
        sessionCode=None
        orderCode=None
        closed=""
        side=None
        symbol=""
        qty=0
        price=0
        priceCode=None
        priceBefore=0
        priceaAfter=0
        orderNo=""
        qtyCurrent=0
        qtyNext=0
        qtyDeal=0
        confirmTime="" 
        code=""
        codeMsg=""
        canCancel=""
        canModify=""
        source=""
        isPreOrder="" 
        settleCode=None
        brokerId=""
        avgPrice=0
        updateTime=""
        state=None
        lastStatus=None
        stateMsg=""
        currency=""
        timeInForce=None
        def __init__(self, seqNo, account, orderTime, orderDate, sessionCode, orderCode, closed, side, symbol, qty, price, priceCode, priceBefore,\
                     priceAfter, orderNo, qtyCurrent, qtyNext, qtyDeal, confirmTime, code, codeMsg, canCancel, canModify, source, isPreOrder, settleCode,\
                     brokerId, avgPrice, updateTime, state, lastStatus, stateMsg, currency, timeInForce):
            """
            Parameters
            ----------
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
            closed : string
                是否收盤.
            side : Enum
                買賣別<Buy=0,Sell=1>.
            symbol : string
                標的代碼.
            qty : integer
                委託量.
            price : decimal
                委託價.
            priceCode : Enum
                價格別<限價=0,市價=1>.
                #平盤=2
                #跌停=3
                #漲停=4    
                #範圍市價=5
            priceBefore : decimal
                改價前委託價.
            priceAfter : decimal
                改價後委託價.
            orderNo : string
                委託書號.
            qtyCurrent : integer
                改量前委託量.
            qtyNext : integer
                改量後委託量.
            qtyDeal : integer
                成交量.
            confirmTime : string
                回報時間.
            code : string
                錯誤代碼.
            codeMsg : string
                錯誤訊息.
            canCancel : string
                可否刪單.
            canModify : string
                可否改量.
            source : string
                來源別.
            isPreOrder : string
                是否為預約單.
            settleCode : Enum
                交割型態<餘客交割=0,逐筆交割=1>.
            brokerId : string
                推薦券商.
            avgPrice : decimal
                成交均價.
            updateTime : string
                異動時間.
            state : Enum
                委託單狀態<收到='0',交易所回覆失敗='9',成功='10',改量='20',刪單='30',全部成交='50',委託失敗='90'>.
            lastStatus : Enum
                最後委託單狀態<收到='0',交易所回覆失敗='9',成功='10',改量='20',刪單='30',全部成交='50',委託失敗='90'>.
            stateMsg : string
                委託單狀態訊息.
            currency : string
                幣別.
            timeInForce : Enum
                委託條件<ROD=0,IOC=1,FOK=2>.

            Returns
            -------
            None.
            """
            self.seqNo=seqNo
            self.account=account
            self.orderTime=orderTime
            self.orderDate=orderDate
            self.sessionCode=SessionCode(sessionCode)
            self.orderCode=OrderCode(orderCode)
            self.closed=closed
            self.side=SideCode(side)
            self.symbol=symbol
            self.qty=qty
            self.price=price
            self.priceCode=PriceCode(priceCode)
            self.priceBefore=priceBefore
            self.priceaAfter=priceAfter
            self.orderNo=orderNo
            self.qtyCurrent=qtyCurrent
            self.qtyNext=qtyNext
            self.qtyDeal=qtyDeal
            self.confirmTime=confirmTime
            self.code=code
            self.codeMsg=codeMsg
            self.canCancel=canCancel
            self.canModify=canModify
            self.source=source
            self.isPreOrder=isPreOrder
            self.settleCode=SettleCode(settleCode)
            self.brokerId=brokerId
            self.avgPrice=agvPrice
            self.updateTime=updateTime
            self.state=OrderState(state)
            self.lastStatus=OrderState(lastStatus)
            self.stateMsg=stateMsg
            self.currency=currency
            self.timeInForce=TimeInForce(timeInForce)