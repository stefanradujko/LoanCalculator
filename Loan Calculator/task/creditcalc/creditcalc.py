from math import log, ceil
import argparse


def izracunaj_diff(principal, periods, interest):
    nominal_interest = interest / (12 * 100)
    suma = 0
    for i in range(1, periods + 1):
        mesecno = ceil(principal / periods + nominal_interest * (principal - (principal * (i - 1) / periods)))
        suma += mesecno
        print(f'Month {i}: payment is {mesecno}')
    print(f'Overpayment = {suma - principal}')


def izracunaj_payment(principal, periods, interest):
    if principal is None or periods is None or interest is None:
        print('Incorrect parameters')
        return
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    nominal_interest = interest / (12 * 100)
    payment = ceil((principal * nominal_interest * (1 + nominal_interest) ** periods)
                   / ((1 + nominal_interest) ** periods - 1))
    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {payment * periods - principal}')


def izracunaj_principal(payment, periods, interest):
    if payment is None or periods is None or interest is None:
        print('Incorrect parameters')
        return
    payment = int(payment)
    periods = int(periods)
    interest = float(interest)
    nominal_interest = interest / (12 * 100)
    principal = ceil(payment / ((nominal_interest * (1 + nominal_interest) ** periods)
                                / ((1 + nominal_interest) ** periods - 1)))
    print(f'Your loan principal = {principal}!')
    print(f'Overpayment = {payment * periods - principal}')


def izracunaj_periods(principal, payment, interest):
    if payment is None or principal is None or interest is None:
        print('Incorrect parameters')
        return
    principal = int(principal)
    payment = int(payment)
    interest = float(interest)
    nominal_interest = interest / (12 * 100)
    od_cega = payment / (payment - nominal_interest * principal)
    periods = ceil(log(od_cega, 1 + nominal_interest))
    ispisi_mesece(periods)
    print(f'Overpayment = {payment * periods - principal}')


def ispisi_mesece(m):
    kusur = m % 12
    god = m // 12
    if god == 0:
        if kusur == 1:
            print(f'It will take {kusur} month to repay this loan!')
        else:
            print(f'It will take {kusur} months to repay this loan!')
    elif god == 1:
        if kusur == 0:
            print(f'It will take {god} year to repay this loan!')
        elif kusur == 1:
            print(f'It will take {god} year and {kusur} month to repay this loan!')
        else:
            print(f'It will take {god} year and {kusur} months to repay this loan!')
    elif god > 1:
        if kusur == 0:
            print(f'It will take {god} years to repay this loan!')
        elif kusur == 1:
            print(f'It will take {god} years and {kusur} month to repay this loan!')
        else:
            print(f'It will take {god} years and {kusur} months to repay this loan!')


def sta_zelis():
    if args.type is None:
        print('Incorrect parameters')
    elif args.type == 'annuity':
        if args.payment is None:
            izracunaj_payment(args.principal, args.periods, args.interest)
        elif args.principal is None:
            izracunaj_principal(args.payment, args.periods, args.interest)
        elif args.periods is None:
            izracunaj_periods(args.principal, args.payment, args.interest)
    elif args.type == 'diff':
        if args.principal is None or args.periods is None or args.interest is None:
            print('Incorrect parameters')
        elif int(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0:
            print('Incorrect paramaters')
        else:
            izracunaj_diff(int(args.principal), int(args.periods), float(args.interest))
    else:
        print('Incorrect parameters')


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()
sta_zelis()
