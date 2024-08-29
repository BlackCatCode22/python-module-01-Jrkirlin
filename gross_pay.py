
hour_weekly = input("Enter hours: ")
pay_rate = input("Enter rate: ")
no_ot_net_pay = float(hour_weekly) * float(pay_rate)
ot_pay_rate = float(pay_rate) * 1.5
ot_net_pay = float(hour_weekly) * ot_pay_rate


if float(hour_weekly) > 40:
    print("Gross pay with overtime:",ot_net_pay)

else:
    print("Gross pay:",no_ot_net_pay)
