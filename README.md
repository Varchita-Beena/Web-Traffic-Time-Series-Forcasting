# Web-Traffic-Time-Series-Forcasting
## Dataset
The problem is of forecasting future web traffic for approximately 145,000 Wikipedia articles. https://www.kaggle.com/c/web-traffic-time-series-forecasting <br>

## Fractal
A curve or geometrical figure, each part of which has the same statistical character as the whole.<br>
![Fractal]()

To evaluate whether data traffic traces follow heavy-tail distributions – an indication of fractal behavior.<br>
Heavy-tail distributions :-  probability distributions those have heavier tails than the exponential distribution. <br> 
Example :- pareto , weibull etc. <br>

![Time Series Plot]()

![Weibull distribution for above time series]()

every datapoint is fractal. The pattern is repeating.

## Methodology 

The series should be Stationary. <br>
Making subsets w.r.t days of week (to find whether the week has fractal shape or not) <br>
Finding Hurst exponent of subsets <br>
	-Hurst exponent is used to measure of long-term memory of time 	series. It is referred as index of dependence.<br>
Putting in bins<br>
Prediction<br>


## Hurst exponent

Calculating the average value, Xm, of the X1..Xn series<br>
Calculating the standard series deviation, S<br>
Normalization of the series by deducting the average value, Zr (where r=1..n), from each value<br>
Creating a cumulative time series Y1=Z1+Zr, where r=2..n<br>
Calculating the magnitude of the cumulative time series R=max(Y1..Yn)-min(Y1..Yn) <br>
Dividing the magnitude of the cumulative time series by the standard deviation (S) <br>


