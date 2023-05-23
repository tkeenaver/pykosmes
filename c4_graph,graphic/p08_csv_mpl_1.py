from matplotlib import pyplot as plt
import csv
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name( )
rc('font', family=font_name)

infile = open("data/weather_input.csv", "r")
data = csv.reader(infile)

x = [ ]
y = [ ]

for line in data:
    x.append(line[0])
    y.append(float(line[2]))

plt.plot(x, y, marker='o')
plt.title("2009년 대관령 월평균 강수량") 
plt.xlabel("월") 
plt.ylabel("강수량(mm)") 
plt.show( )
infile.close( )
