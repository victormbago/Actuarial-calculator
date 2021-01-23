import wholelifeassurance
import termassurance
import pureendowemt
import endowmentassurance


def has_user_selected_to_finish():
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish Assurances? press  (y) '
                           'to continue with Assurances   press n:  ').lower()
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be  (y) or (n). Please try again')
    return ok_to_finish


def assurance_interface():
    finish = False
    while not finish:
        print('=' * 50)
        print('ASSURANCE OPTIONS ARE: \n:'
              '\t 1. WHOLE LIFE\n'
              '\t 2. TERM ASSURANCES\n'
              '\t 3. PURE ENDOWMENT  ASSURANCES \n'
              '\t 4. ENDOWMENT ASSURANCES \n')
        print('=' * 50)
        assurance_option = int(input('CHOOSE ONE TO COMPUTE:'))
        print('=' * 50)
        if assurance_option == 1:  # whole life
            payment_time = int(input('ULTIMATE TABLES OR SELECT :\n'
                                     '\t 1. ULTIMATE\n'
                                     '\t 2. SELECT \n'))
            print('=' * 50)
            if payment_time == 1:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    wholelifeassurance.wholelife_at_end_year_am92_ultimate()
                if tables_option == 2:
                    wholelifeassurance.wholelife_at_end_year_a196770_ultimate()
            if payment_time == 2:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    wholelifeassurance.wholelife_immediately_on_death_am92_select()
                if tables_option == 2:
                    wholelifeassurance.wholelife_immediately_on_death_a196770_select()
        if assurance_option == 2:
            payment_time = int(input('ULTIMATE TABLES OR SELECT :\n'
                                     '\t 1. ULTIMATE\n'
                                     '\t 2. SELECT \n'))
            print('=' * 50)
            if payment_time == 1:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    termassurance.term_at_end_year_am92_ultimate()
                if tables_option == 2:
                    termassurance.term_at_end_year_a196770_ultimate()
            if payment_time == 2:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    termassurance.term_immediately_on_death_am92_select()
                if tables_option == 2:
                    termassurance.term_immediately_on_death_a196770_select()

        if assurance_option == 3:  # pure endowment
            payment_time = int(input('ULTIMATE TABLES OR SELECT :\n'
                                     '\t 1. ULTIMATE\n'
                                     '\t 2. SELECT \n'))
            print('=' * 50)
            if payment_time == 1:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    pureendowemt.pure_endowment_at_end_year_am92_ultimate()
                if tables_option == 2:
                    pureendowemt.pure_endowment_at_end_year_a196770_ultimate()
            if payment_time == 2:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    pureendowemt.pure_endowment_immediately_on_death_am92_select()
                if tables_option == 2:
                    pureendowemt.pure_endowment_immediately_on_death_a196770_select()

        if assurance_option == 4:  # endowment assurance
            payment_time = int(input('ULTIMATE TABLES OR SELECT :\n'
                                     '\t 1. ULTIMATE\n'
                                     '\t 2. SELECT \n'))
            print('=' * 50)
            if payment_time == 1:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    endowmentassurance.pure_endowment_at_end_year_am92_ultimate()
                if tables_option == 2:
                    endowmentassurance.pure_endowment_at_end_year_a196770_ultimate()
            if payment_time == 2:
                tables_option = int(input('Enter calculation  basis :\n'
                                          '\t 1. AM92\n'
                                          '\t 2. A1967-70\n'))
                print('=' * 50)
                if tables_option == 1:
                    endowmentassurance.pure_endowment_immediately_on_death_am92_select()
                if tables_option == 2:
                    endowmentassurance.pure_endowment_immediately_on_death_a196770_select()

            print('=' * 50)

        print('=' * 50)
        finish = has_user_selected_to_finish()
