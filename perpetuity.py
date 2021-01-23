import am92
import amm19
import a55females
import a55males


def perpetuity_deffered_advance():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t AM 92\n'
                      '2.\t A1967-70\n'
                      '3.\t A(55) MALES\n'
                      '4.\t A(55)FEMALES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_deferred_advance_perpetuity()
    if basis == 2:
        amm19.tables_A196770_deferred_advance_perpetuity()
    if basis == 3:
        a55males.tables_deferred_advance_perpetuity()
    if basis == 4:
        a55females.tables_deferred_advance_perpetuity()


def perpetuity_deffered_arrears():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t AM 92\n'
                      '2.\t A1967-70\n'
                      '3.\t A(55) MALES\n'
                      '4.\t A(55)FEMALES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_deferred_arrears_perpetuity()
    if basis == 2:
        amm19.tables_A196770_deferred_arrears_perpetuity()
    if basis == 3:
        a55males.tables_deferred_arrears_perpetuity()
    if basis == 4:
        a55females.tables_deferred_arrears_perpetuity()


def perpetuity_advance():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t AM 92\n'
                      '2.\t A1967-70\n'
                      '3.\t A(55) MALES\n'
                      '4.\t A(55)FEMALES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_advance_perpetuity()
    if basis == 2:
        amm19.tables_A196770_advance_perpetuity()
    if basis == 3:
        a55males.tables_advance_perpetuity()
    if basis == 4:
        a55females.tables_advance_perpetuity()


def perpetuity_arrears():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t AM 92\n'
                      '2.\t A1967-70\n'
                      '3.\t A(55) MALES\n'
                      '4.\t A(55)FEMALES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_arrears_perpetuity()
    if basis == 2:
        amm19.tables_A196770_arrears_perpetuity()
    if basis == 3:
        a55males.tables_arrears_perpetuity()
    if basis == 4:
        a55females.tables_arrears_perpetuity()


def perpetuity_continously_advance():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t ELT 12 FELAMES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_advance_continosly_perpetuity()


def perpetuity_continously_arrears():
    basis = int(input('what is the calculation basis::\n'
                      '1.\t ELT 12 FELAMES\n'
                      ))
    print('=' * 50)
    if basis == 1:
        am92.tables_arrears_continosly_perpetuity()
