def segitiga():
    bintang = 8
    print((bintang) * "* ")
    for i in range(bintang-1, 1, -1):
        print((bintang-i-1)* " " +  "*" + (2*i -1)*" " + "* ")
    print((bintang-1) * " " + "* ")


segitiga()