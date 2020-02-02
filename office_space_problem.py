from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

f,n =[int(i) for i in raw_input().strip().split()]
x_data  = []
y_data = []
x_data_test = []
for i in range (0,n):
    temp = [float(val) for val in raw_input().strip().split()]
    x_data.append( temp[:-1] )
    y_data.append(temp[-1:][0])
model = make_pipeline(PolynomialFeatures(3), LinearRegression())
model.fit(x_data, y_data)


T = int(raw_input().strip())
for i in range(0,T):
    x_data_test.append( [float(val) for val in raw_input().strip().split()])

y_predict = model.predict(x_data_test)

for element in y_predict:
    print round(element,2)

