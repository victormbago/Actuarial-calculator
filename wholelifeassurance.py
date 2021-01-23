
import xlrd

loc = "tables.xlsx"  # this is the file location.
wb = xlrd.open_workbook(loc)


def wholelife_at_end_year_am92_ultimate():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(0)  # opens the first work book of the excel file
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)  # loops within the column
        if x == num:
            dx = sheet.cell_value(num - 1, 2)  # location of the value of Dx
            mx = sheet.cell_value(num - 1, 10)  # location of the Mx value
            print('Dx is : ', dx)
            print('Mx is : ', mx)
            ann = mx / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def wholelife_at_end_year_a196770_ultimate():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            mx = sheet.cell_value(num, 9)
            print('Dx is : ', dx)
            print('Mx is : ', mx)
            ann = mx / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def wholelife_immediately_on_death_am92_select():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(0)  # opens the first work book of the excel file
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)  # loops within the column
        if x == num:
            dx = sheet.cell_value(num - 1, 1)  # location of the value of Dx
            mx = sheet.cell_value(num - 1, 8)  # location of the Mx value
            print('Dx is : ', dx)
            print('Mx is : ', mx)
            ann = mx / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)


def wholelife_immediately_on_death_a196770_select():  # for payments made at the end of the year of death
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num+2, 2)
            mx = sheet.cell_value(num+2, 8)
            print('Dx is : ', dx)
            print('Mx is : ', mx)
            ann = mx / dx
            final_answer = sum_assured * ann
            print(f'Assurance value is {ann}')
            print('Final Assurance  value is : ', final_answer)
