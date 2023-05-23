import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
#import matplotlib.font_manager
#fn=matplotlib.font_manager.get_font_names()
#plt.rc('font', family='NanumGothicCoding')
plt.rc('font', family='Batang')

#weather = pd.read_csv('data/weather.csv', encoding='CP949')
weather = pd.read_csv('data/weather_u.csv', encoding='UTF-8')

weather['일시'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('일시').mean()
means['평균풍속'].plot()

plt.show()