import openpyxl

wb = openpyxl.load_workbook("scpl.xlsx")

sheets = wb.sheetnames
print(wb.active.title)
sh = wb['#LN00011']
data = sh['B3'].value

print(data)