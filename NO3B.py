def jumlahHurufKonsonan(hruf):
    konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstwxyz"
    b = 0
    hasil = 0
    for i in hruf:
        if i in konsonan:
            b += len(i)
        else:
            b += 0
    hasil = len(hruf),b
    return hasil
