import openpyxl
import os

cwd = os.getcwd()
filename = "df.xlsx"
filepath = os.path.join(cwd, "data", filename)

#워크북(Workbook) 객체
wb = openpyxl.load_workbook(filepath)   
print(wb.sheetnames)

#시트(Sheet) 객체
ws = wb['Sheet1']
print(ws)
print(ws.title)

active_sheet = wb.active
print(active_sheet)