def Ksqrt(num):
    return KRoot().mySqrt(num)


def mySpilt(num):
    mantysa, wykladnik = ("{:,24e}".format(num)).split("e")
    return float(mantysa), int(wykladnik)


class KRoot:
    sqrt10 = 3.162277660168379331998894

    def __init__(self):
        self.count = 0

    def mySqrtDec(self, x):
        self.count = 0
        sqrtAprx = 0.562 + x * (0.468 + (-0.0313 + 0.00104 * x) * x)
        sqrtOld = sqrtAprx
        while True:
            sqrtNew = (sqrtOld + x / sqrtOld) / 2
            if sqrtNew == sqrtOld:
                break
            sqrtOld = sqrtNew
            self.count += 1
        return sqrtNew

    def mySqrt(self, x):
        if 0 <= x < 10:
            return self.mySqrtDec(x)
        else:
            mant, expon = mySplit(x)
            k = int(expon / 2)
            corr = expon - 2 * k
            c = 1
            if expon == 2 * k + 1:
                c = self.sqrt10
            return self.mySqrtDec(mant) * 10 ** k * c


def KadaptRK3BS(XY):
    global h, FIO, nbad, nok, nowy_stan
    x, *Y = XY
    hstare = h
    k1 = [h * num for num in FIO]
    k2 = [h * num for num in F(x + 0.5 * h, *(Yi + 0.5 * ki for Yi, ki in zip(Y, k1)))]
    k3 = [h * num for num in F(x + 0.75 * h, *(Yi + 0.75 * ki for Yi, ki in zip(Y, k2)))]
    Y3 = [Yi + (2 * k1i + 3 * k2i + 4 * k3i) / 9 for Yi, k1i, k2i, k3i in zip(Y, k1, k2, k3)]
    FIOnowe = F(x + h, *Y3)
    k4 = [h * num for num in FIOnowe]
    DeltaY23 = [abs((5 * k1[i] - 6 * k2[i] - 8 * k3[i] + 9 * k4[i]) / 72) for i in range(len(k1))]
    DeltaK = max(DeltaY23[i] / (0.5 * (abs(Y[i]) + abs(Y3[i])) + abs(Y3[i] - Y[i])) for i in range(len(Y3)))
    h = hstare * (delta / DeltaK) ** (1 / 3)
    if DeltaK > delta:
        nbad += 1
        nowy_stan = False
        return XY
    else:
        FIO = FIOnowe
        nok += 1
        nowy_stan = True
        return [x + hstare] + Y3
