##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## test_Usage
##

from sources.main import print_usage


class TestUsage:

    usage = "USAGE\n\t./308reedpipes r0 r5 r10 r15 r20 n\n"\
          "DESCRIPTION\n"\
          "\tr0\tradius (in cm) of pipe at the 0cm abscissa\n"\
          "\tr5\tradius (in cm) of pipe at the 5cm abscissa\n"\
          "\tr10\tradius (in cm) of pipe at the 10cm abscissa\n"\
          "\tr15\tradius (in cm) of pipe at the 15cm abscissa\n"\
          "\tr20\tradius (in cm) of pipe at the 20cm abscissa\n"\
          "\tn\tnumber of points needed to display the radius\n"

    def test_usagePrint(self, capsys):
        print_usage()
        stdout = capsys.readouterr()[0]
        assert stdout == self.usage
