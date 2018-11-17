from datetime import date, timedelta


def beetWeenDays():

    d1 = date(2018, 11, 1)
    d2 = date(2018, 11, 5)

    delta = d2 - d1         # timedelta

    for i in range(delta.days + 1):
        print(d1 + timedelta(i))


beetWeenDays()