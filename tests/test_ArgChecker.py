##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## test_ArgChecker
##

from sources.ArgChecker import ArgChecker


class TestArgChecker:
    def test_objCreation(self):
        tArgChecker = ArgChecker()
        assert tArgChecker.get_args_list() is None

    def test_ErrorCheck(self):
        tArgChecker = ArgChecker()
        assert not tArgChecker.check_args_types(['a', 'b', 'c', 'd', 'e', 'f'])
        assert tArgChecker.get_args_list() is None

    def test_typeError(self, capsys):
        tArgChecker = ArgChecker()
        assert not tArgChecker.check_args_types(['1.2', '2.5', '3', '4', '5', '5.0'])
        assert tArgChecker.get_args_list() is None
        stdout = capsys.readouterr()[0]
        assert stdout == "ValueError: ArgChecker.py:21\ninvalid literal for int() with base 10: '5.0'\n"

    def test_negativeNumbers(self):
        tArgChecker = ArgChecker()
        assert not tArgChecker.check_args_types(['1.2', '-2.5', '3', '4', '5', '-5'])
        assert tArgChecker.get_args_list() is None

    def test_validArguments(self):
        tArgChecker = ArgChecker()
        assert tArgChecker.check_args_types(['1.2', '2.5', '3', '4', '5', '5'])
        assert tArgChecker.get_args_list() == [1.2, 2.5, 3, 4, 5, 5]
