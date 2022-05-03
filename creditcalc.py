import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument("-pay", "--payment", type=float)
parser.add_argument("-prin", "--principal", type=float)
parser.add_argument("-per", "--periods", type=float)
parser.add_argument("-int", "--interest", type=float)

args = parser.parse_args()


# ask = input("""What do you want to calculate?
# type "n" - for number of monthly payments,
# type "a" - for annuity monthly payment amount,
# type "p" - for the monthly payment:""")

if args.periods == None and args.interest == None:
    print('Incorrect parameters.')

else:
    if args.periods == None:
        i = args.interest / (12*100)
        base = args.payment / (args.payment - i * args.principal)
        n = math.ceil(math.log(base, 1 + i))
        number_months = n % 12
        number_years = n // 12
        if number_months < 12 and number_years == 0:
            print(f"It will take {n} months to repay the loan!")
        elif number_months == 1 and number_years == 0:
            print(f"It will take {n} month to repay the loan!")
        elif number_years == 1 and number_months == 0:
            print(f"It will take 1 year to repay the loan!")
        elif number_years == 1 and number_months == 1:
            print("It will take 1 year and 1 month to repay the loan!")
        elif number_years == 1 and number_months > 1:
            print(f"It will take 1 year and {number_months} months to repay the loan!")
        elif number_years > 1 and number_months == 0:
            print(f"It will take {number_years} years to repay the loan!")
        else:
            print(f"It will take {number_years} years and {number_months} months to repay the loan!")
        overpayment = n * args.payment - args.principal
        print(f"Overpayment = {overpayment}")

    if args.type == "annuity" and args.payment == None:
        i = args.interest / (12 * 100)
        annuity_payment = math.ceil(args.principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
        overpayment = math.ceil((annuity_payment * args.periods) - args.principal)
        print(f"Your annuity payment = = {annuity_payment}!")
        print(f"Overpayment = {overpayment}")


    if args.type == "diff" and args.interest != None:
        i = args.interest / (12 * 100)
        m = 1
        sum_d = 0
        while m != args.periods + 1:
            D = math.ceil((args.principal / args.periods) + i * (args.principal - ((args.principal * (m - 1)) / args.periods)))
            print(f"Month {m}: payment is {D}")
            m += 1
            sum_d += D
        overpayment = math.ceil(sum_d - args.principal)
        print(f"\nOverpayment = {overpayment}")

    if args.principal == None:
        i = args.interest / (12 * 100)
        x = ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
        loan_principal = args.payment / x
        loan_principal_pr = math.floor(loan_principal)
        print(f"Your loan principal = {loan_principal_pr}!")
        annuity_payment = math.floor(loan_principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
        overpayment = math.ceil((annuity_payment * args.periods) - loan_principal)
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
