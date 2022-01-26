##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## main


class Reedpipe:
    def __init__(self, args: list) -> None:
        self._vectorIdx = [x for x in range(0, 25, 5)]
        self._data_set = args[:-1]
        self._n = args[-1]
        self._vector = [float(0) for _ in range(5)]

        self._pointAbscissas = [float(0) for _ in range(self._n)]
        self._radiusValues = [float(0) for _ in range(self._n)]
        pass

    def _computeVectorComponents(self) -> None:
        x = float(0)
        y = float(0)
        z = float(0)

        x = 6 * (self._data_set[2] - 2 * self._data_set[1] + self._data_set[0]) / 50
        y = 6 * (self._data_set[3] - 2 * self._data_set[2] + self._data_set[1]) / 50
        z = 6 * (self._data_set[4] - 2 * self._data_set[3] + self._data_set[2]) / 50
        self._vector[2] = (y - (x + z) / 4) * 4 / 7
        self._vector[3] = z / 2 - 0.25 * self._vector[2]
        self._vector[1] = x / 2 - 0.25 * self._vector[2]

        def getPointAbscissa(index: int) -> float:
            return 20 / (self._n - 1) * index

        def getRadiusAtAbscissa() -> float:
            f = int((abscissaAtI - 0.01) / 5) + 1
            return (-self._vector[f - 1] / 30 * pow(abscissaAtI - self._vectorIdx[f], 3)
                    + self._vector[f] / 30 * pow(abscissaAtI - self._vectorIdx[f - 1], 3)
                    - (self._data_set[f - 1] / 5 - 5 / 6 * self._vector[f - 1])
                    * (abscissaAtI - self._vectorIdx[f])
                    + (self._data_set[f] / 5 - 5 / 6 * self._vector[f])
                    * (abscissaAtI - self._vectorIdx[f - 1]))

        for i in range(self._n):
            abscissaAtI = getPointAbscissa(i)
            self._pointAbscissas[i] = abscissaAtI
            self._radiusValues[i] = getRadiusAtAbscissa()

    def _displayResults(self) -> None:
        print(f'vector result: [{self._vector[0]:.1f}, {self._vector[1]:.1f}, {self._vector[2]:.1f}, '
              f'{self._vector[3]:.1f}, {self._vector[4]:.1f}]')
        for i in range(self._n):
            print(f'abscissa: {self._pointAbscissas[i]:.1f} cm\tradius: {self._radiusValues[i]:.1f} cm')

    def runEngine(self) -> bool:
        self._computeVectorComponents()
        self._displayResults()
