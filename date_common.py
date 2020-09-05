

from datetime import datetime, date, timedelta
import calendar


# 今天和昨天
today = date.today() # 今天
today_str = datetime.strftime(today, '%Y-%m-%d')
yesterday = today - timedelta(days=1)	# 昨天
yesterday_str = datetime.strftime(yesterday, '%Y-%m-%d')


# 0.日期初始化
data_basic_str = '2017-10-18'				# 基准日期，全脚本【唯一需修改】的地方

date0 = datetime.strptime(data_basic_str, '%Y-%m-%d')
year0, month0, day0 = date0.year, date0.month, date0.day		# 年 月 日


# 0.基准日期本身
month0_str = str(year0) + '-0' + str(month0) if month0 < 10 else str(year0) + '-' + str(month0)	# 年-月 str

week0, dayofweek0 = date0.isocalendar()[1:] 													# 周 周内第几天
week0_str = str(year0) + '-0' + str(week0) if week0 < 10 else str(year0) + '-' + str(week0) 	# 年-周 str

quarter0 = month0 / 3 if month0 % 3 == 0 else int(month0 / 3) + 1	# 季度
quarter0_str = str(year0) + '-0' + str(quarter0)			 		# 年-季度 str


# 1.上下月
# 1.1 上月今天
year01 = year0 - 1 if month0 == 1 else year0 					# 上月-年
month01 = 12 if month0 == 1 else month0 - 1						# 上月-月
day01 = min(day0, calendar.monthrange(year01, month01)[1])		# 上月-日 今天
thisday_lastmonth = date0.replace(year=year01, month=month01, day=day01)	# 上月今天
thisday_lastmonth_str = datetime.strftime(thisday_lastmonth, '%Y-%m-%d')	# 上月今天 str


# 1.2 下月今天
year02 = year0 + 1 if month0 == 12 else year0 					# 下月-年
month02 = 1 if month0 == 12 else month0 + 1 					# 下月-月
day02 = min(day0, calendar.monthrange(year02, month02)[1]) 		# 下月-日 今天
thisday_nextmonth = date0.replace(year=year02, month=month02, day=day02)
thisday_nextmonth_str = datetime.strftime(thisday_nextmonth, '%Y-%m-%d')	# 下月的今天 str


# 2.日期变换
date_before_n = date0 - timedelta(days=n)					# n天前日期

# 2.1 周
thisday_lastweek = date0 - timedelta(days=7) 				# 上周今天
thismonday = date0 - timedelta(days=date0.weekday()) 		# 本周一
thissunday = date0 - timedelta(days=date0.weekday() - 6)	# 本周日
lashmonday = date0 - timedelta(days=date0.weekday() + 7)	# 上周一

# 2.2 月
nthday_thismonth = date0.replace(day=n)		# 本月n号
thisday_nthmonth = date0.replace(month=n)	# n月今天

firstday_thismonth = date0.replace(day=1)										# 本月1号
lastday_thismonth = date0.replace(day=calendar.monthrange(year0, month0)[1])	# 本月最后1天
lastday_lastmonth = firstday_thismonth - timedelta(days=1)						# 上月最后1天
firstday_lastmonth = lastday_lastmonth.replace(day=1)							# 上月1号
firstday_nextmonth = lastday_thismonth + timedelta(days=1)						# 下月1号
lastday_nextmonth = firstday_nextmonth.replace(day=calendar.monthrange(firstday_nextmonth.year, firstday_nextmonth.month)[1])  # 下月最后1天


# 3. 通用方法
date_str = datetime.strftime(date_int, '%Y-%m-%d') 	# 格式日期 --> 字符串
date_int = datetime.strptime(date_str, '%Y-%m-%d') 	# 字符串 --> 格式日期