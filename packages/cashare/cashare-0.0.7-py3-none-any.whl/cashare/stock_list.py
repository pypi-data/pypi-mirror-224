import httpx
from cashare.common.dname import url1
import pandas as pd


def stock_list(token,type:str):
    if type in['us','hk','ca']:
        url = url1 + '/stock/list/'+type+'/'+ token
        r = httpx.get(url,timeout=100)
        return pd.DataFrame(r.json())
    else:
        return "type输入错误"

if __name__ == '__main__':
    df=stock_list(type='hk',token='')
    print(df)
    df = stock_list(type='ca', token='')
    print(df)
    df = stock_list(type='us', token='')
    print(df)
    pass



