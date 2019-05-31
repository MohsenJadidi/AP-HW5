import numpy as np

class PyGaussSolver:
    def __init__(self, func, a, b, n):
        self.func = func
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
            return ((2 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((m_N - 1) / m_N) * self.legendre(m_N - 2, x)

    def dLegendre(self, m_N, x):
        LegendrePrime = ( m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x))
        return LegendrePrime

    def legendreZeroes(self, m_N, i):
        xNew, xOld = 0, 0
        xOld = np.cos(3.141592655 * (i - 1 / 4) / (m_N + 1 / 2))
        iteration = 1
        while True:

            if iteration != 1:
                xOld = xNew
            xNew = xOld - self.legendre(m_N, xOld)/ self.dLegendre(m_N, xOld)
            iteration += 1
            if (1 + abs((xNew - xOld))) > 1:
                break
        return xNew

    def weight(self, m_N, x):
        weightI = 2 / ((1 - x ** 2) * (self.dLegendre(m_N, x))**2)
        return weightI

    def exec(self):
        iteration = 2
        integral = 0
        for i in range(1, self.m_N + 1):
            integral = integral + self.func(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N, self.legendreZeroes(self.m_N, i))
        self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral

    def getResult(self):
        return self.m_Result