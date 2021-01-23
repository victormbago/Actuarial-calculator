import xlrd

loc = "tables.xlsx"  # this is the file location.
wb = xlrd.open_workbook(loc)


def tables_advance_perpetuity():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured=int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nx = sheet.cell_value(num - 1, 5)
            print('Dx is : ', dx)
            print('Nx is : ', nx)
            ann = nx / dx
            final_answer=sum_assured*ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_arrears_perpetuity():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nxn = sheet.cell_value(num, 5)
            print('Dx is : ', dx)
            print('Nx+1 is : ', nxn)
            ann = nxn / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_advance_term():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('enter term duration i.e n :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nx = sheet.cell_value(num - 1, 5)
            nxn = sheet.cell_value((num - 1) + n, 5)
            print('Dx is : ', dx)
            print('Nx is : ', nx)
            print('Nx+n is : ', nxn)
            ann = (nx - nxn) / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_arrears_term():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('enter n :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nx = sheet.cell_value(num, 5)
            nxn = sheet.cell_value(num + n, 5)
            print('Dx is : ', dx)
            print('Nx+1 is : ', nx)
            print('Nx+n+1 is : ', nxn)
            ann = (nx - nxn) / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_deferred_advance_perpetuity():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nm = sheet.cell_value((num - 1) + m, 5)
            print('Dx is : ', dx)
            print('Nx+m is : ', nm)
            ann = nm / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_deferred_arrears_perpetuity():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nm = sheet.cell_value(num + m, 5)
            print('Dx is : ', dx)
            print('Nx+m+1 is : ', nm)
            ann = nm / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_deferred_advance_term():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    n = int(input('enter term period i.e n :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nm = sheet.cell_value((num - 1) + m, 5)
            nxm = sheet.cell_value((num - 1) + (m + n), 5)
            print('Dx is : ', dx)
            print('Nx+m is : ', nm)
            print('Nx+m+n is : ', nxm)
            ann = (nm - nxm) / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)


def tables_deferred_arrears_term():
    sheet = wb.sheet_by_index(3)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    n = int(input('enter term period i.e n :'))
    sum_assured = int(input('enter sum assured amount : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num - 1, 4)
            nm = sheet.cell_value(num + m, 5)
            nxm = sheet.cell_value(num + (m + n), 5)
            print('Dx is : ', dx)
            print('Nx+m+1 is : ', nm)
            print('Nx+m+n+1 is : ', nxm)
            ann = (nm - nxm) / dx
            final_answer = sum_assured * ann
            print(f'Annuity value is {ann}')
            print('Final annuity value is : ', final_answer)