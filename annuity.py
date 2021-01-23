import perpetuity
import term
import time


def has_user_selected_to_finish():
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish annuities (y) '
                           'to continue with annuities  press n:  ').lower()
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be  (y) or (n). Please try again')
    return ok_to_finish


def annuity_interface():
    finish = False
    while not finish:

        print('=' * 50)
        print('=' * 50)
        print('Annuity options are :')
        print('\t 1. Term annuities')
        time.sleep(1.5)
        print('\t 2. perpetuities')
        time.sleep(1)
        print('\t 3. deferred annuities')
        time.sleep(0.5)
        print('=' * 50)
        option = int(input('pick one that you want to compute: '))
        # if option not in ('1', '2', '3'):
        #   print('invalid entry try again')
        print('=' * 50)
        if option == 1:
            toption = int(input('\t1. Payable in Advance:\n'
                                '\t2. Payable in Arrears:\n'
                                '\t3. Payable continuously:\n'))
            print('=' * 50)
            if toption == 1:
                term.Term_advance()
            if toption == 2:
                term.Term_arrears()
            if toption == 3:
                term.Term_continously()

        if option == 2:
            poption = int(input('\t1. Perpetuity Payable in Advance:\n'
                                '\t2. Perpetuity Payable in Arrears:\n'
                                '\t3. Payable continously:\n'))
            print('=' * 50)
            if poption == 1:
                perpetuity.perpetuity_advance()
            if poption == 2:
                perpetuity.perpetuity_arrears()
            if poption == 3:
                nem = int(input('\tWe have continuously :\n'
                                '\t1. Continuously payable in advance:\n '
                                '\t2. Continuously payable in arrears :\n'))
                if nem == 1:
                    perpetuity.perpetuity_continously_advance()
                if nem == 2:
                    perpetuity.perpetuity_continously_arrears()

        if option == 3:
            coption = int(input('\t1. Deferred Term\n'
                                '\t2. Deferred perpetuity\n'))
            print('=' * 50)
            if coption == 1:
                ccoption = int(input('\t1. Deferred term payable in advance: \n'
                                     '\t2. Deferred term payable in arrears:\n'))
                print('=' * 50)
                if ccoption == 1:
                    term.deffered_term_advance()
                if ccoption == 2:
                    term.deffered_term_arrears()
            if coption == 2:
                cooption = int(input('\t1. Deferred perpetuity payable in advance: \n'
                                     '\t2. Deferred perpetuity payable in arrears:\n'))
                print('=' * 50)
                if cooption == 1:
                    perpetuity.perpetuity_deffered_advance()
                if cooption == 2:
                    perpetuity.perpetuity_deffered_arrears()

        print('=' * 50)
        finish = has_user_selected_to_finish()
