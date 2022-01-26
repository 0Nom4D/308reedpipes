##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## t_ArgChecker

from sources.Reedpipe import Reedpipe
from sources.exitCode import exitCode


class TestExitCodes:
    def test_okCode(self):
        assert not exitCode.OK

    def test_errorCode(self):
        assert exitCode.ERROR == 84


class TestReedpipe:
    def test_objCreation(self):
        tPipe = Reedpipe([2, 3, 2, 4, 5, 13])
        assert tPipe._n == 13
        assert tPipe._vectorIdx == [0, 5, 10, 15, 20]
        assert tPipe._data_set == [2, 3, 2, 4, 5]
        assert tPipe._vector == [0.0, 0.0, 0.0, 0.0, 0.0]
        assert tPipe._pointAbscissas == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        assert tPipe._radiusValues == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
