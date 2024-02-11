def KAdapt53(a, c, b, fa, fc, fb, func, eps):
    global count

    h = (b - a) / 2
    ac = (a + c) / 2
    fac = func(ac)
    cb = (c + b) / 2
    fcb = func(cb)

    s3 = h * (fa + 4 * fc + fb) / 3  # pojedynczy krok 3-rzędu
    s5 = h * (fa + 4 * fac + 2 * fc + 4 * fcb + fb) / 6  # podwóny krok 3-rzędu
    Integ = (16 * s5 - s3) / 15  # krok 5-rzędu

    if abs(s3 - s5) < eps * abs(s5):
        count += 1
        return Integ  # s5

    else:
        return KAdapt53(a, ac, c, fa, fac, fc, func, eps) + \
            KAdapt53(c, cb, b, fc, fcb, fb, func, eps)
count=0