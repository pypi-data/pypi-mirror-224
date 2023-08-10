# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:30:23 2022

@author: Cheryl.fan
"""

import json
import enum
import inspect
import datetime
import logging.config
import os
from .ObjJsonEncoding import *
from .EasyPyenum import *
from .SendMsg import *
from .EasyPyEvent import *
from .QueryPy import *

logconf_file = os.path.join(os.path.dirname(__file__), 'easypy.config')
logging.config.fileConfig(logconf_file)
logger = logging.getLogger('MainLogger')        
filehandler = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.date.today()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
filehandler.setFormatter(formatter)        

'''
TradePy為交易用類別
規劃可供委託的金融市場:證券, 期貨, 海外期貨, 複委託及保證金交易
'''
class TradePy:
    systemCode="EasyPy" #系統代碼
    tradeState=None #委託狀態
    cusDiffCode=None #顧客自定義
    exchangeCode = None #交易所別
    className="TradePy" #型別名稱    
    sales="0000" #營業員代碼
    xMarket=None #x市場
    serialNo="0" #委託序號
    tradeSerial=None #辨識碼   
    def __init__(self, address: str="127.0.0.1", sales: str="0000"):
        """       
        Parameters
        ----------
        address : string, optional
            Server IP address. The default is "127.0.0.1".        
        sales : string, optional
            營業員代碼. The default is "0000".
        Returns
        -------
        None.
        """
        global send
        global query
        logger.info("Start TradePy!!!")
        self.xMarket="init"
        self.sales = sales
        self.TradeeventsREQ = EventsHandler()
        self.TradeeventsSUB = EventsHandler()      
        send = SendMsg(address)
        send.eventsREQ.Changed += self.req_changed
        send.eventsSUB.Changed += self.sub_changed
        query = QueryPy(address)
    
    '''
    股票交易
    '''
    def stock(self, account, symbol, price, qty, seqNo: str="", orderNo: str="", side: SideCode=0, tradeCode: TradeCode=0,\
              orderCode: OrderCode=0, priceCode: PriceCode=0, sessionCode: SessionCode=0, timeinForce: TimeInForce=0,\
              commodityCode: CommodityCode=0, branchId: str="0000", cusDiffCode: str="None"):
        """       
        Parameters
        ----------
        account : string
            帳號.
        symbol : string
            標的代碼.
        price : decimal
            委託價.
        qty : integer
            委託量.
        seqNo : string, optional
            網路流水號. The default is "".
        orderNo : string, optional
            委託單號. The default is "".
        side : SideCode Enum, optional
            買賣別<Buy=0,Sell=1>. The default is 0.
        tradeCode : TradeCode Enum, optional
            交易別<Order=0,Cancel=1,ChgPX=2,ChgQty=3>. The default is 0.
        orderCode : OrderCode Enum, optional
            委託別< 現股=0 ,融資=1,融券=2,先賣沖=22>. The default is 0.
            #代辦融資=4
            #代辦融券=5
        priceCode : PriceCode Enum, optional
            價格別<限價=0,市價=1>. The default is 0.      
            #平盤=2
            #跌停=3
            #漲停=4    
            #範圍市價=5
        sessionCode : SessionCode Enum, optional
            盤別<普通=0,零股=1,盤後定盤=2,盤中零股=7>. The default is 0.
        timeinForce : TimeInForce Enum, optional
            委託條件<ROD=0,IOC=1,FOK=2>. The default is 0.
        commodityCode : CommodityCode Enum, optional
            商品別<TSE=0, OTC=1>. The default is 0.
            #FUT=2
            #OPT=3
            #OSTK=4
            #OFUT=5
            #OOPT=6
            #FOREIGN=7
        branchId : string, optional
            分公司. The default is "0000".
        cusDiffCode : string, optional
            顧客自定義. The default is "None".

        Returns
        -------
        None.
        """
        try:
            self.cusDiffCode=cusDiffCode
            self.serialNo="%08d" % (int(self.serialNo) + 1)
            self.tradeSerial="STK" + self.serialNo
            self.exchangeCode=ExchangeCode.TWSE
            self.xMarket=Stocks(tradeCode, symbol, account, orderCode, priceCode, sessionCode, timeinForce, price, qty,\
                                   side, commodityCode, seqNo, orderNo, branchId)
            self.__sendTrade(self.jsonFormat())
        except Exception as e:
            logger.error("stk error:" + str(e))
            
    def req_changed(self, sender, msg):
        self.TradeeventsREQ.change(msg)
        
    def sub_changed(self, sender, msg):
        self.TradeeventsSUB.change(msg)
           
    '''
    送出交易資料
    '''
    def __sendTrade(self, jsonStr):
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
            return json.dumps(self, cls=ObjJsonEncoding, sort_keys=True, indent=4, ensure_ascii=False) # 換行
        else:
            return json.dumps(self, cls=ObjJsonEncoding, sort_keys=True, ensure_ascii=False) #不換行

    '''
    取得交易回覆訊息
    '''
    def QueryRequest(self, account: str):
        query.queryItem(send, account)


'''
Stocks證券市場
為設定證券市場在進行委託時所需提供的參數
Python類別可供動態擴充
'''
class Stocks:
    marketCode=MarketCode.Stocks #市場別
    commodityCode=None #商品別
    branchId="" #分公司代碼
    symbol="" #股票代碼  
    account="" #帳號
    tradeCode=TradeCode.Order #交易別    
    xTrade = None #x交易        
    def __init__(self, tradeCode, symbol, account, orderCode, priceCode, sessionCode, timeinForce, price, qty, side,\
                 commodityCode, seqNo, orderNo, branchId):
        """
        Parameters
        ----------
        tradeCode : Enum
            交易別<Order=0,Cancel=1,ChgPX=2,ChgQty=3>.     
        symbol : string
            標的代碼.
        account : string
            帳號.
        orderCode : Enum
            委託別< 現股=0 ,融資=1,融券=2,先賣沖=22>.
            #代辦融資=4
            #代辦融券=5
        priceCode : Enum
            價格別<限價=0,市價=1>.     
            #平盤=2
            #跌停=3
            #漲停=4    
            #範圍市價=5
        sessionCode : Enum
            盤別<普通=0,零股=1,盤後定盤=2,盤中零股=7>.
        timeinForce : Enum
            委託條件<ROD=0,IOC=1,FOK=2>.
        price : decimal
            委託價.
        qty : integer
            委託量.
        side : Enum, 
            買賣別<Buy=0,Sell=1>.
        commodityCode : Enum
            商品別<TSE=0, OTC=1>
            #FUT=2
            #OPT=3
            #OSTK=4
            #OFUT=5
            #OOPT=6
            #FOREIGN=7
        seqNo : string
            網路流水號.
        orderNo : string
            委託單號.
        branchId : string
            分公司.

        Returns
        -------
        None.
        """
        try:
            self.tradeCode = TradeCode(tradeCode)
            self.symbol=symbol
            self.account=account
            self.commodityCode=CommodityCode(commodityCode)
            self.branchId=branchId           
            self.__select(orderCode, priceCode, sessionCode, timeinForce, price, qty, side, seqNo, orderNo)    
        except Exception as e:
            raise
    
    '''
    選擇交易別: Order, Cancel, Replace
    '''
    def __select(self, orderCode, priceCode, sessionCode, timeinForce, price, qty, side, seqNo, orderNo):
        if self.tradeCode == TradeCode.Order:
            self.xTrade = self.Order(orderCode, priceCode, sessionCode, timeinForce, price, qty, side)
        if self.tradeCode == TradeCode.Cancel:
            self.xTrade = self.Cancel(orderCode, priceCode, sessionCode, timeinForce, price, qty, side, orderNo, seqNo)
        if self.tradeCode == TradeCode.ChgPX or self.tradeCode == TradeCode.ChgQty:
            self.xTrade = self.Replace(ChangeCode.PX if self.tradeCode == TradeCode.ChgPX else ChangeCode.QTY,\
                                        orderCode, priceCode, sessionCode, timeinForce, price, qty, side, orderNo, seqNo)
                   
    '''
    委託
    '''       
    class Order:
        side=SideCode.Buy #買賣別
        orderDate=None #交易日
        orderCode=OrderCode.現股 #委託
        priceCode=PriceCode.限價 #價格別
        sessionCode=SessionCode.普通 #盤別
        timeinForce=TimeInForce.ROD #委託條件
        price=0 #委託價
        qty=0 #委託量     
        xType=None #型別
        def __init__(self, orderCode, priceCode, sessionCode, timeinForce, price, qty, side):
            """
            Parameters
            ----------
            orderCode : Enum
                委託別< 現股=0 ,融資=1,融券=2,先賣沖=22>.
                #代辦融資=4
                #代辦融券=5
            priceCode : Enum
                價格別<限價=0,市價=1>.     
                #平盤=2
                #跌停=3
                #漲停=4    
                #範圍市價=5
            sessionCode : Enum
                盤別<普通=0,零股=1,盤後定盤=2,盤中零股=7>.
            timeinForce : Enum
                委託條件<ROD=0,IOC=1,FOK=2>.
            price : decimal
                委託價.
            qty : integer
                委託量.
            side : Enum, 
                買賣別<Buy=0,Sell=1>.

            Returns
            -------
            None.
            """
            try:
                self.xType= "order"
                self.orderDate=datetime.date.today().strftime("%Y%m%d")
                self.orderCode=OrderCode(orderCode)
                self.priceCode=PriceCode(priceCode)
                self.sessionCode=SessionCode(sessionCode)
                self.timeinForce=TimeInForce(timeinForce)
                self.price=price
                self.qty=qty
                self.side=SideCode(side)
            except Exception as e:
                raise
    
    '''
    刪單
    '''
    class Cancel:      
        orderDate=None #交易日
        side=SideCode.Buy #買賣別
        orderCode=OrderCode.現股 #委託
        priceCode=PriceCode.限價 #價格別
        sessionCode=SessionCode.普通 #盤別
        timeinForce=TimeInForce.ROD #委託條件
        price=0 #委託價
        qty=0 #委託量    
        orderNo=None #委託單號       
        serialId="" #網路流水號
        xType=None #型別
        def __init__(self, orderCode, priceCode, sessionCode, timeinForce, price, qty, side, orderNo, seqNo):
            """
            Parameters
            ----------
            orderCode : Enum
                委託別< 現股=0 ,融資=1,融券=2,先賣沖=22>.
                #代辦融資=4
                #代辦融券=5
            priceCode : Enum
                價格別<限價=0,市價=1>.     
                #平盤=2
                #跌停=3
                #漲停=4    
                #範圍市價=5
            sessionCode : Enum
                盤別<普通=0,零股=1,盤後定盤=2,盤中零股=7>.
            timeinForce : Enum
                委託條件<ROD=0,IOC=1,FOK=2>.
            price : decimal
                委託價.
            qty : integer
                委託量.
            side : Enum, 
                買賣別<Buy=0,Sell=1>.
            orderNo : string
                委託書號.
            seqNo : string
                網路流水號.

            Returns
            -------
            None.
            """
            try:
                self.xType= "cancel"
                self.orderDate=datetime.date.today().strftime("%Y%m%d")
                self.orderCode=OrderCode(orderCode)
                self.priceCode=PriceCode(priceCode)
                self.sessionCode=SessionCode(sessionCode)
                self.timeinForce=TimeInForce(timeinForce)
                self.price=price
                self.qty=qty
                self.seqNo=seqNo
                self.orderNo=orderNo
                self.side=SideCode(side)
            except Exception as e:
                raise
            
            
    '''
    修改:改價, 改量
    '''
    class Replace:   
        changeCode=ChangeCode.PX #修改別
        orderDate=None #交易日
        side=SideCode.Buy #買賣別
        orderCode=OrderCode.現股 #委託別
        priceCode=PriceCode.限價 #價格別
        sessionCode=SessionCode.普通 #盤別
        timeinForce=TimeInForce.ROD #委託條件
        price=0 #委託價
        qty=0 #委託量     
        serialId="" #網路流水號
        orderNo=None #委託單號
        xType=None #型別
        def __init__(self, changeCode, orderCode, priceCode, sessionCode, timeinForce, price, qty, side, orderNo, seqNo):
            """
            Parameters
            ----------
            changeCode : Enum
                修正別<PX=0,QTY=1>.
            orderCode : Enum
                委託別< 現股=0 ,融資=1,融券=2,先賣沖=22>.
                #代辦融資=4
                #代辦融券=5
            priceCode : Enum
                價格別<限價=0,市價=1>.     
                #平盤=2
                #跌停=3
                #漲停=4    
                #範圍市價=5
            sessionCode : Enum
                盤別<普通=0,零股=1,盤後定盤=2,盤中零股=7>.
            timeinForce : Enum
                委託條件<ROD=0,IOC=1,FOK=2>.
            price : decimal
                委託價.
            qty : integer
                委託量.
            side : Enum, 
                買賣別<Buy=0,Sell=1>.
            orderNo : string
                委託書號.
            seqNo : string
                網路流水號.

            Returns
            -------
            None.
            """
            try:
                self.xType= "replace"            
                self.orderDate=datetime.date.today().strftime("%Y%m%d")
                self.orderCode=OrderCode(orderCode)
                self.priceCode=PriceCode(priceCode)
                self.sessionCode=SessionCode(sessionCode)
                self.timeinForce=TimeInForce(timeinForce)
                self.price=price
                self.qty=qty
                self.seqNo=seqNo
                self.orderNo=orderNo
                self.side=SideCode(side)
                self.changed(changeCode)
            except Exception as e:
                raise
            
        '''
        確認: 改價, 改量
        '''
        def changed(self, changeCode):
            self.changeCode=changeCode
            if self.changeCode == ChangeCode.PX:
                self.xType="changePX"
            if self.changeCode == ChangeCode.QTY:
                self.xType="changeQTY"
                                            