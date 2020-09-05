#!/usr/bin/env python3

#-----------------------------------------------------------------
# 时间：2018-07-12
# 版本：0.1
# 内容：
#	1.日期工具类			刘尧	2018-07-12
#	2.无监督权重算法		刘尧	2018-07-12
#	3.地理位置工具类		刘尧	2018-07-12
#
# 备注：无
#-----------------------------------------------------------------

import sys
import os
from pandas import DataFrame,Series
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from math import log
from datetime import datetime,date,timedelta
import calendar


#1.日期工具类
#代码实现
class dataUtils():
	def __init__(self, date0_str):
		if date_str is None:
			date0 = date.today() 		#当前日期默认今天，也可为任意一天
			date0_str = str(date0)
		else:
			date0 = datetime.strptime(date0_str, '%Y-%m-%d')
	
	#间隔n天的日期
	def ndays(n):
		return date0+timedelta(days=n)
	
	#昨天日期
	def yesterday(format='%Y-%m-%d'):
		return datetime.strftime(ndays(-1), format)
	
	#明天日期
	def tomorrow(format='%Y-%m-%d'):
		return datetime.strftime(ndays(1), format)

	#上月今天
	#下月今天
	#本月1号
	#本月最后1天
	#上月1号
	#上月最后1天
	#下月1号
	#下月最后1天
	#上周今天
	#下周今天
	#本周一
	#本周日
	#其他……



#2.无监督权重算法
#代码实现
class weightCalculator():
    def __init__(self, df):
        scaler = MinMaxScaler(feature_range=(0, 100))
        df_scaled = DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index) #一定要保证colunms特别是index的一致
        df_corr = df_scaled.corr()
        df_stat = DataFrame([df_scaled.apply(lambda x: np.sqrt(np.var(x)))], index=['sd'])  #标准差
        df_stat = df_stat.append(Series(df_scaled.mean(), name='mean'))                     #均值
        df_stat = df_stat.append(Series(df_scaled.apply(self.get_entropy), name='entropy')) #熵值
        self.df_stat = df_stat.append(Series(df_corr.applymap(lambda x: 1-x).sum(), name='critic_part'))  #CRITIC部分
        self.df = df
        self.scaler = scaler        #归一标尺
        self.df_scaled = df_scaled  #归一后数据,格式跟df完全一致
    
    def get_entropy(self, se):
        p = se/se.sum()
        tmp = p.apply(lambda x: 0 if x==0 else x*log(x))
        return 1 + tmp.sum()/log(se.size)

	#熵权法
    def weight_entropy(self):
        ent = self.df_stat.ix['entropy']
        return ent/ent.sum()
    
	#标准离差法
    def weight_sd(self):
        sd = self.df_stat.ix['sd']
        return sd/sd.sum()

	#信息量权数法
    def weight_sdmean(self):
        tmp = Series(self.df_stat.ix['sd']/self.df_stat.ix['mean'], name='sdmean')
        return tmp/tmp.sum()
    
	#CRITIC法
    def weight_critic(self):
        critic = Series(self.df_stat.ix['sd']*self.df_stat.ix['critic_part'], name='critic')
        return critic/critic.sum()

#使用示例
def weightCalculatorDemo():
    d2 = DataFrame({'a':[3,2,5,1,6], 'b':[3,6,7,9,1], 'c':[5,7,2,1,5]})
    d2['c'] = d2['c']*(-1)
    wc = weightCalculator(d2)
    print(wc.weight_entropy())
    print(wc.weight_sd())
    print(wc.weight_critic())
    print(wc.weight_sdmean())



#3.地理位置工具类
R = 6371393				#地球直径
#根据坐标计算两点球面距离
def sphere_distance(x1, y1, x2, y2):
	xx1 = x1 * 3.1415926 / 180
	yy1 = y1 * 3.1415926 / 180
	xx2 = x2 * 3.1415926 / 180
	yy2 = y2 * 3.1415926 / 180
	return R * acos(cos(xx1) * cos(xx2) * cos(yy1 - yy2) + sin(xx1) * sin(xx2))
