from cashare.common.dname import url1
import pandas as pd
from cashare.common.get_data import _retry_get
def u_h_now_data(type,token):
    li = handle_url(type=type, token=token)
    r =_retry_get(li,timeout=100)
    if str(r) == 'token无效或已超期':
        return r
    else:
        return r
def handle_url(type,token):
    g_url=url1+'/us/stock/nowprice/'+type+'/'+token
    return g_url
if __name__ == '__main__':
    ll=u_h_now_data(type='all',token='')
    print(ll)



