'''
Created on 2015-5-6

@author: skt
'''

import numpy as np 

'''
用户-游戏的影响因子
由以下参数组成
点击数, 支付金额, 购买订单
'''
def getFactor(logincount, smsCount, totalMoney):
    factor = 0.0
