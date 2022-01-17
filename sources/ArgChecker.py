##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## ArgChecker


class ArgChecker:
    def __init__(self) -> None:
        self._args = None
        pass

    def check_args_types(self, args: list) -> bool:
        self._args = list()

        for number in args:
            try:
                value = float(number)
            except ValueError as error:
                self._args = None
                print(f"ValueError: ArgChecker.py:21\n{error.args[0]}")
                return False
            self._args.append(value)
        if any(i <= 0 for i in self._args):
            self._args = None
            return False
        return True

    def get_args_list(self) -> list:
        return self._args
