# This file is one of pure endowment,One is eligible for pay here if they survive till the end of the term
# of the contract.

import xlrd

loc = "tables.xlsx"  # this is the file location.
wb = xlrd.open_workbook(loc)


def pure_endowment_at_end_year_am92_ultimate():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(0)  # opens the first work book of the excel file
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n=int(input('Enter term duration :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)  # loops within the column
        if x == num:
            dx = sheet.cell_value(num - 1, 2)  # location of the value of Dx
            dxn= sheet.cell_value((num - 1+n), 2)  # location of the Mx value
            print('Dx is : ', dx)
            print('Dx+n is : ', dxn)
            ann = dxn/ dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def pure_endowment_at_end_year_a196770_ultimate():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('Enter term duration :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            dxn = sheet.cell_value((num+n), 1)
            print('Dx is : ', dx)
            print('Dx+n is : ', dxn)
            ann = dxn / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def pure_endowment_immediately_on_death_am92_select():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(0)  # opens the first work book of the excel file
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('Enter term duration :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)  # loops within the column
        if x == num:
            dx = sheet.cell_value(num - 1, 1)  # location of the value of Dx
            dxn = sheet.cell_value((num - 1+n), 1)  # location of the Mx value
            print('Dx is : ', dx)
            print('Dx+n is : ', dxn)
            ann = dxn / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def pure_endowment_immediately_on_death_a196770_select():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('Enter term duration :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num + 2, 2)
            dxn = sheet.cell_value((num + 2+n), 2)
            print('Dx is : ', dx)
            print('Dx+n is : ', dxn)
            ann = dxn / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)
