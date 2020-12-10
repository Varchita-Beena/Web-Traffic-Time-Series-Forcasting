import pandas as pd
import numpy as np
import math
import matplotlib.pylab as plt
from datetime import datetime
import nolds
def parser(x):
	return datetime.strptime(x,'%Y-%m-%d')
data = pd.read_csv('se_1.csv', header=None, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
ts = pd.Series(data)
dates = list(ts.index)
hits = list(ts.values)
dates_7 = dates[0:6]
def makingsubsets(num):
	day = num
	dict_day = {}
	while day < 458:
		dict_day[dates[day]] = hits[day]
		day = day + 7
	return dict_day
dict = makingsubsets(0)
monday_series = pd.Series(dict)
plt.plot(ts)
plt.show()

dict = makingsubsets(1)
tuesday_series = pd.Series(dict)
dict = makingsubsets(2)
plt.plot(monday_series)
plt.show()
wednesday_series = pd.Series(dict)
dict = makingsubsets(3)
thursday_series = pd.Series(dict)
dict = makingsubsets(4)
friday_series = pd.Series(dict)
dict = makingsubsets(5)
saturday_series = pd.Series(dict)
dict = makingsubsets(6)
sunday_series = pd.Series(dict)

t = np.array((monday_series.values),dtype = float)
t1 = np.array((tuesday_series.values),dtype = float)
t2 = np.array((wednesday_series.values),dtype = float)
t3 = np.array((thursday_series.values),dtype = float)
t4 = np.array((friday_series.values),dtype = float)
t5 = np.array((saturday_series.values),dtype = float)
t6 = np.array((sunday_series.values),dtype = float)

hurst = []
hurst.append(nolds.hurst_rs(t))
hurst.append(nolds.hurst_rs(t1))
hurst.append(nolds.hurst_rs(t2))
hurst.append(nolds.hurst_rs(t3))
hurst.append(nolds.hurst_rs(t4))
hurst.append(nolds.hurst_rs(t5))
hurst.append(nolds.hurst_rs(t6))
list_1 = []
list_2 = []
list_3 = []
bin_1 = []
bin_2 = []
bin_3 = []
def calbin(index,bin):
	if index == 0:
		return np.concatenate((bin,np.array(monday_series)),axis = 0)
	elif index == 1:
		return np.concatenate((bin,np.array(tuesday_series)),axis = 0)
	elif index == 2:
		return np.concatenate((bin,np.array(wednesday_series)),axis = 0)
	elif index == 3:
		return np.concatenate((bin,np.array(thursday_series)),axis = 0)
	elif index == 4:
		return np.concatenate((bin,np.array(friday_series)),axis = 0)
	elif index == 5:
		return np.concatenate((bin,np.array(saturday_series)),axis = 0)
	else: return np.concatenate((bin,np.array(sunday_series)),axis = 0)
for i,each in enumerate(hurst):
	if each < 0.5:
		list_1.append(i)
		bin_1 = calbin(i,np.array(bin_1))
	elif each > 0.5 and each < 1.0:
		list_2.append(i)
		bin_2 = calbin(i,np.array(bin_2))
	else:
		list_3.append(i)
		bin_3 = calbin(i,np.array(bin_3))

data1 = pd.read_csv('out_1.csv', header=None, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
ts_test = pd.Series(data1)
print ts_test.head()
dates_train =  dates[0:7]
dates_test = list(ts_test.index)
hits_test = list(ts_test.values)
predictions = []

bin1 = pd.Series(bin_1)
bin2 = pd.Series(bin_2)
bin3 = pd.Series(bin_3)

for each in dates_test:
	temp = []
	temp1 = []
	d1 = str(each.date())
	d2 = d1.split("-")
	for litle in d2:
		temp.append(int(litle))
	for i,every in enumerate(dates_train):
		d3 = str(every.date())
		d4 = d1.split("-")
		for lil in d4:
			temp1.append(int(lil))
		diff = [x1 - x2 for (x1, x2) in zip(temp, temp1)]
		if diff[0] == 0 and diff[1] == 0 and diff[2] == 0: 
			at = i
			break
	if at in list_1:
		predictions.append(float((bin1.sample(n=1)).values))
	elif at in list_2:
		predictions.append(float((bin2.sample(n=1)).values))
	else:
		#print at
		predictions.append(float((bin3.sample(n=1)).values))

		
error = [x1 - x2 for (x1, x2) in zip(predictions, hits_test)]
error_abs = []
for each in error:
	error_abs.append(abs(each))
mse = np.mean(np.array(error_abs))
sum =0
for each in error_abs:
	sum = sum + (each * each)
rmse = math.sqrt(sum / len(predictions))
print rmse
print predictions[0:5]
print error_abs[0:5]
print predictions
print hits_test




