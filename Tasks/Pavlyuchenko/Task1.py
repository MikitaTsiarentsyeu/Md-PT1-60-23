print('CALCULATION OF THE TOTAL DEPOSIT AMOUNT \n  FILLING RULES: (...)\n ')
while True:
    answ = int(input('Would u like to continue? (1 - Yes, 0 - No): '))

    if answ == 1:
        amount1 = float(input('---Enter the initial amount,$: '))
        term = int(input('---Enter the term, years: '))
        per = float(input('---Enter the annual per, %: '))

        def final_amount(P, T, i):
            amount2 = P * T * (1+i/100)
            if P < 0 or T < 0:
                print(' •The initial amount and term must be > 0!\n')
            elif i < 0:
                print(' •NEGATIVE PER! The total amount of the deposit,$: {amount2: 2.2f},$ \n')
            else:
                print(f' •The total amount of the deposit,$: {amount2: 2.2f} \n')
        final_amount(amount1, term, per)

    elif answ == 0:
        print('Thank for your attention! COME BACK =)')
        break
    else:
        print('Unknown command =(\n(1 - Yes, 0 - No)\n')