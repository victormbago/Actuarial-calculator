import annuity
import assuranceinterface
import about
import braintest


def back_to_main_menu():
    main_menu = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('TO GO TO MAIN MENU PRESS :m: ').lower()
        if user_input == 'm':
            main_menu = False
            user_input_accepted = True
        else:
            print('Response must be  (m). Please try again')
    return main_menu


finish = False
while not finish:
    print('=' * 50)
    print('=' * 50)
    print(
        '\t     MAIN MENU\n'
        '\t 1. CALCULATIONS\n'
        '\t 2. BRAIN TEST\n'
        '\t 3. ABOUT \n'
        '\t 4. EXIT\n')
    print('=' * 50)
    g_option = int(input('ENTER OPTION:\n'))
    print('=' * 50)
    if g_option == 1:
        c_option = int(input('WHAT DO YOU WANT TO  COMPUTE: \n'
                             '\t 1. LIFE ANNUITIES \n'
                             '\t 2. ASSURANCES \n'
                             '\t 3. INTEREST RATES \n'
                             '\t 4. ANNUITY CERTAIN \n'
                             '\t 5. PRESENT VALUE \n'
                             '\t 6. ACCUMULATION \n'
                             '\t 7. LIFE TABLE FUNCTIONS \n'
                             '\t 8. GROSS PREMIUMS \n'))
        if c_option == 1:
            annuity.annuity_interface()
        if c_option == 2:
            assuranceinterface.assurance_interface()
    if g_option == 2:
        braintest.test_function(braintest.questions)
    if g_option == 3:
        about.about_of_program()
    finish = back_to_main_menu()
