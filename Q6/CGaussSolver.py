import math


class CGaussSolver:
    def __init__(self, func, a, b, n):
        self.m_func = func
        self.m_A = a
        self.m_B = b
        self.m_N = n
        self.m_Result = None

    def legendre(self, m_N, x):
        if m_N == 0:
            return 1
        elif m_N == 1:
            return x
        else:
            return ((2.0 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((1.0 * m_N - 1) / m_N) * self.legendre(m_N - 2, x)

    def dLegendre(self, m_N, x):
        dLegendre = (1.0 * m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x))
        return dLegendre

    def legendreZeroes(self, m_N, i):
        xnew1, xold1 = 0, 0
        pi = 3.141592655
        xold1 = math.cos(pi * (i - 1 / 4.0) / (m_N + 1 / 2.0))

        xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)

        while (1 + math.fabs((xnew1 - xold1))) > 1.:
            xold1 = xnew1
            xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)

        return xnew1

    def weight(self, m_N, x):
        weightI = 2 / ((1 - pow(x, 2)) * pow(self.dLegendre(m_N, x), 2))
        return weightI

    def exex(self):
        iteration = 2
        integral = 0

        for i in range(self.m_N + 1):
            integral = integral + self.m_func(self.legendreZeroes(self.m_N, i)) \
                       * self.weight(self.m_N, self.legendreZeroes(self.m_N, i))

        self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral

    def getResult(self):
        return self.m_Result


