from datetime import date, timedelta


def hari():

    tanggal_pertama = date(2018, 11, 1)
    tanggal_kedua = date(2018, 11, 5)

    delta = tanggal_kedua - tanggal_pertama

    for i in range(delta.days + 1):
        print(tanggal_pertama + timedelta(i))

hari()