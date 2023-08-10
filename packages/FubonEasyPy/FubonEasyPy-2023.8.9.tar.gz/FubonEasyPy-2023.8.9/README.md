# python


## 相依性

pyzmq>=23.1, !=23.1.1, <=25.1

https://pyip.org/project/pyzmq/

nest-asyncio>=1.4.3, !=1.5.0, <=1.6

https://pyip.org/project/nest-asyncio/

persizmq>=1.0, !=1.0.0, <=1.0.3

https://pypi.org/project/persizmq/



## 描述

使用MessageQueue技術進行跨平台跨程序間的訊息傳遞,
主要的功能是讓Python用戶可以對FubonAPI套件傳遞交易訊息, 
再由FubonAPI套件與Fubon E01API進行交易串接.

EasyPy我們使用了許多非同步及多執行緒來處理訊息傳遞, 
以確保交易訊息傳遞過程式花費最少的等待時間, 且可必免訊息阻塞.

之後, 我們會再陸續更新EasyPy功能, 如支援期貨交易, 提供經濟數據查詢.



## 安裝

```
python -m pip install FubonEasyPy
```

Python3.10.x <3.11


## 使用

```
from FubonEasyPy import *

def req_changed(sender, msg):
   print('%s' % msg)

def sub_changed(sender, msg):
   print('%s' % msg)
   
t = TradePy("xxx.xxx.xxx.xxx")

t.TradeeventsREQ.Changed += req_changed
t.TradeeventsSUB.Changed += sub_changed

# 交易
t.stock(account="xxxxx", symbol="1101", price=50, qty=1)

#查詢
t.QueryRequest(account="xxxxx")
```

TradePy(Address:)

Address:為FubonAPI套件的主機位址。



## 更版記錄

2023.8.0