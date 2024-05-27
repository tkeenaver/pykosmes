import openpyxl
from openpyxl.formatting.rule import ColorScaleRule

wb = openpyxl.Workbook()
ws = wb.active

for row in range(1, 11):
    ws[f'A{row}'] = row

rule = ColorScaleRule(start_type='min', start_color='FF0000', end_type='max', end_color='00FF00')
ws.conditional_formatting.add('A1:A10', rule)

file_path = "output/conditional_formatting.xlsx"
wb.save(file_path)
