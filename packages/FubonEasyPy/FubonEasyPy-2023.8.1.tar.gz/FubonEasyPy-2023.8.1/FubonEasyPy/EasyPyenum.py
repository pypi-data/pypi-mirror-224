# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:36:37 2022

@author: Cheryl.fan
"""
import enum

'''
市場型態
'''
class MarketCode(enum.Enum):
    Stocks=0
    #SubBorkerages=1
    Futures=2
    #OverseasFurutes=3
    #Foreigns=4
    
'''
交易所型態, 複委託及海期請直接給交易所代碼
'''
class ExchangeCode(enum.Enum):
    TWSE=0
    TAIFEX=1
    FOR=2
    #複委託, 海期依交易所別

'''
交易型態
'''
class TradeCode(enum.Enum):
    Order = 0
    Cancel = 1
    ChgPX = 2
    ChgQty = 3

'''
委託型態
'''
class OrderCode(enum.Enum):
    現股=0 
    融資=1
    融券=2
    先賣沖=22
    #代辦融資=4
    #代辦融券=5

'''
價格型態
'''
class PriceCode(enum.Enum):
    限價=0
    市價=1
    範圍市價=2
    #平盤=2
    #跌停=3
    #漲停=4        
    
'''
盤別型態
'''
class SessionCode(enum.Enum):
    普通=0
    零股=1
    盤後定盤=2    
    盤中零股=7
    
'''
委託條件
'''
class TimeInForce(enum.Enum):
    ROD=0
    IOC=1
    FOK=2
    
'''
修改型態
'''
class ChangeCode(enum.Enum):
    PX=0
    QTY=1
    
'''
買賣型態
'''
class SideCode(enum.Enum):
    Buy=0
    Sell=1
    
'''
部位型態
'''
class PositionCode(enum.Enum):
    新倉=0
    平倉=1
    自動=2
    當沖=3
    
'''
商品型態
'''
class CommodityCode(enum.Enum):
    TSE=0
    OTC=1
    #FUT=2
    #OPT=3
    #OSTK=4
    #OFUT=5
    #OOPT=6
    #FOREIGN=7      
    
'''
單種型態
'''
class OrderKind(enum.Enum):
    FUTSingle=0
    FUTCompound=1
    OPTSingle=2
    OPTCompound=3
    
'''
買賣權型態
'''
class CallPutCode(enum.Enum):
    Non=0 
    Call=1
    Put=2

'''
回報型態
'''
class GroupCode(enum.Enum):
    回覆="00"
    委託="03"
    成交="04"

'''
作業型態
'''
class OperationCode(enum.Enum):
    預約失敗="02"
    委託成功="11"
    委託失敗="12"
    刪單成功="21"
    刪單失敗="22"
    改量成功="31"
    改量失敗="32"
    成交="40"

'''
交割型態
'''
class SettleCode(enum.Enum):
    餘客交割=0
    逐筆交割=1
    
'''
下單型態
'''
class ProgramCode(enum.Enum):
    通知=1
    一般單回報=2
    智慧單回報=3
    
'''
成交量旗標型態
'''
class DealFlagCode(enum.Enum):
    依據盤別=0
    皆為股數=1
    
'''
查詢型態
'''
class QueryCode(enum.Enum):
    交易日=0   
    庫存=1
    成交單=2
    委託單=3
    權益數=4
    
'''
查詢回報型態
'''
class ReportCode(enum.Enum):
    全部=0
    上市櫃=1
    
'''
查詢交易日型態
'''
class DtKindCode(enum.Enum):
    證券=1
    期權=2
    
'''
狀態型態
'''
class StateCode(enum.Enum):
    盤中=0
    預約=1
    暫停=2
    
'''
查詢委託單狀態
'''
class OrderState(enum.Enum):
    收到='0'
    交易所回覆失敗='9'
    成功='10'
    改量='20'
    刪單='30'
    全部成交='50'
    委託失敗='90'

'''
回覆功能碼型態
'''    
class FunctionCode(enum.Enum):
    一式回報=0
    二式回報委託=1
    二式回報成交=2
    查詢交易日=3
    查詢庫存=4
    查詢委託單=5
    查詢成交單=6
    查詢權益數=7
    
    