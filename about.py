import time


def about_of_program():
    print('This program has been duly coded  by Victor with a main intention of easing some of the \n'
          'calculations done in a normal class setting\n'
          'Tables values used here have been extracted from the 2002 tables and 1908 tables\n'
          'For all selections here, kindly note that one has to input only integer selections like(1,2,3...)')
    print('='*150)
    time.sleep(1.5)
    print(
          'A.ANNUITIES... \n'
          '\t This program only deals with level annuities \n'
          '\t The program computes both the Annuity value and the final annuity value(after multiplying with the sum'
          '\t amount given by the user)\n'
          '\t the tables values used here are only the ones applicable with the 4% interest rate\n'
          '\t For annuities, they only tables in use here are :\n'
          '\t 1. AM92\n'
          '\t 2. A1967-70\n'
          '\t 3. ELT 12 MALES FOR THOSE CONTINUOUSLY PAYABLE\n'
          '\t 4. a(55)Males\n'
          '\t 5. a(55)Females\n')
    print('=' * 150)
    time.sleep(1.3)
    print('B. ASSURANCE..\n'
          '\t The program only deals with level Assurances\n'
          '\t The program computes both the Assurance values from the tables and the final Assurance value(after'
          '\t multiplying with the sum assured value entered\n'
          '\t The program computes both ultimate and select values for any of the Assurances picked \n'
          '\t For both of the cases payments are computes as they are paid at the end of the year of death\n'
          '\t For the tables in this section, they are all in reference to 4% interest rate\n'
          '\t The one payable immediately on death will be available soon\n '
          '\t Tables in use here include :\n'
          '\t 1. AM92 \n'
          '\t 2. A1967-70\n')
