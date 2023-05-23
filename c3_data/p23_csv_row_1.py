import csv     
 
f = open('data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다.
header = next(data)
for row in data: 
    print(row[3], end=',') 
f.close()