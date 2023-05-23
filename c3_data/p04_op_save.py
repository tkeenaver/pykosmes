import openpyxl
import os

#워크북(Workbook) 객체 만들기
wb = openpyxl.Workbook()   
print(wb.sheetnames)

#워크북의 변경내용을 새로운 파일에 저장
wb.save(os.path.join(os.getcwd(), "output", "create_workbook.xlsx"))
print("\n*** output 폴더의 \"create_workbook.xlsx\" 파일을 확인해 보세요. ***\n")
