import csv
import xlrd
import xlwt
import pandas
import openpyxl
workbook = openpyxl.load_workbook('A:\download\月下旬入库表.xlsx')
# print(workbook.sheetnames)
sheet = workbook['7月下旬入库表']
cell = sheet['A1:A5']
for cells in cell:
    print(cells)
    print(cells[0].value)

# xls = xlrd.open_workbook('A:\download\月下旬入库表.xlsx')
# table = xls.sheet_by_name('7月下旬入库表')
# print(table.cell_value(0,0))