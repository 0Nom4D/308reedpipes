#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## main

from sources.ArgChecker import ArgChecker
from sources.Reedpipe import Reedpipe
from sources.exitCode import exitCode
from sys import argv


def print_usage() -> int:
    print("USAGE\n\t./308reedpipes r0 r5 r10 r15 r20 n\n"
          "DESCRIPTION\n"
          "\tr0\tradius (in cm) of pipe at the 0cm abscissa\n"
          "\tr5\tradius (in cm) of pipe at the 5cm abscissa\n"
          "\tr10\tradius (in cm) of pipe at the 10cm abscissa\n"
          "\tr15\tradius (in cm) of pipe at the 15cm abscissa\n"
          "\tr20\tradius (in cm) of pipe at the 20cm abscissa\n"
          "\tn\tnumber of points needed to display the radius"
          )
    return exitCode.OK


def main() -> int:
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help'):
        return print_usage()
    elif len(argv) != 7:
        return exitCode.ERROR
    arg_handler = ArgChecker()
    if not arg_handler.check_args_types(argv[1:]):
        return exitCode.ERROR
    my_engine = Reedpipe(arg_handler.get_args_list())
    my_engine.runEngine()
    return exitCode.OK


if __name__ == '__main__':
    exit(main())
