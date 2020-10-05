from sys import argv


calc_work, wrk_h, rate_per_hour, prize = argv


payment = (int(wrk_h) * int(rate_per_hour) + int(prize))
print(f'Ваша зароботная плата составила: {payment}')
