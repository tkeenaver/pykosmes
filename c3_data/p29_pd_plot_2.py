import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('data/weather.csv', encoding='CP949')
weather['일시'] = pd.DatetimeIndex(weather['일시']).month
# 다음과 같은 groupby() 기능을 사용해서 더 간단한 코드 작성가능
means = weather.groupby('일시').mean()

#plt.plot(means['평균풍속'], 'red')
means['평균풍속'].plot()
plt.show()
