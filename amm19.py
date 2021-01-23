import xlrd

loc = "tables.xlsx"  # this is the file location.
wb = xlrd.open_workbook(loc)


def tables_A196770_advance_perpetuity():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nx = sheet.cell_value(num, 5)
            print('Dx is : ', dx)
            print('Nx is : ', nx)
            ann = nx / dx
            print(f'Annuity value is {ann}')
           


def tables_A196770_arrears_perpetuity():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nx = sheet.cell_value((num + 1), 5)
            print('Dx is : ', dx)
            print('Nx+1 is : ', nx)
            ann = nx / dx
            print(f'Annuity value is {ann}')


def tables_A196770_advance_term():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('enter term duration i.e n :'))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nx = sheet.cell_value(num, 5)
            nxn = sheet.cell_value((num + n), 5)
            print('Dx is : ', dx)
            print('Nx is : ', nx)
            print('Nx+n is : ', nxn)
            ann = (nx - nxn) / dx
            print(f'Annuity value is {ann}')
            

def tables_A196770_arrears_term():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    n = int(input('enter term duration i.e n :'))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nx = sheet.cell_value((num + 1), 5)
            nxn = sheet.cell_value((num + n + 1), 5)
            print('Dx is : ', dx)
            print('Nx+1 is : ', nx)
            print('Nx+n+1 is : ', nxn)
            ann = (nx - nxn) / dx
            print(f'Annuity value is {ann}')


def tables_A196770_deferred_advance_perpetuity():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nm = sheet.cell_value((num + m), 5)
            print('Dx is : ', dx)
            print('Nx+m is : ', nm)
            ann = nm / dx
            print(f'Annuity value is {ann}')
            


def tables_A196770_deferred_arrears_perpetuity():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
  
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nm = sheet.cell_value((num + m + 1), 5)
            print('Dx is : ', dx)
            print('Nx+m+1 is : ', nm)
            ann = nm / dx
            print(f'Annuity value is {ann}')
            


def tables_A196770_deferred_advance_term():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    n = int(input('enter duration of the term : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nm = sheet.cell_value((num + m), 5)
            nxm = sheet.cell_value((num + m + n), 5)
            print('Dx is : ', dx)
            print('Nx+m is : ', nm)
            print('Nx+m+n is : ', nxm)
            ann = (nm - nxm) / dx
            print(f'Annuity value is {ann}')
            


def tables_A196770_deferred_arrears_term():
    sheet = wb.sheet_by_index(1)
    sheet.cell_value(0, 0)
    num = int(input('enter the age of the life:'))
    m = int(input('enter period of deferment i.e m :  :'))
    n = int(input('enter duration of the term : '))
    print('=' * 50)
    for i in range(sheet.nrows):
        x = sheet.cell_value(i, 0)
        if x == num:
            dx = sheet.cell_value(num, 1)
            nm = sheet.cell_value((num + m + 1), 5)
            nxm = sheet.cell_value((num + m + n + 1), 5)
            print('Dx is : ', dx)
            print('Nx+m+1 is : ', nm)
            print('Nx+m+n+1 is : ', nxm)
            ann = (nm - nxm) / dx
            print(f'Annuity value is {ann}')
          
