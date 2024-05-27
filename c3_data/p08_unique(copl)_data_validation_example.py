#copilot의 독특한 답변
import pandas as pd

# 데이터 프레임 생성
df = pd.DataFrame({'Pet Type': ['Dog', 'Cat', 'Hamster'],
                   'Select Pet': ['Dog', 'Cat', 'Hamster']})

# xlsxwriter 엔진으로 Excel 파일 작성
writer = pd.ExcelWriter('output/cop_data_validation.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# xlsxwriter 객체 가져오기
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# 드롭다운 리스트를 위한 데이터 유효성 객체 생성
dropdown_list = ['Dog', 'Cat', 'Hamster']
data_validation = workbook.data_validation({'validate': 'list',
                                            'source': dropdown_list})

# B 열에 데이터 유효성 객체 적용
worksheet.data_validation('B2:B4', data_validation)

# 파일 저장
writer.save()
