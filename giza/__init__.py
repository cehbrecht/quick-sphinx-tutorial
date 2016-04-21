"""This is a Python demo for the `Sphinx tutorial <http://quick-sphinx-tutorial.readthedocs.org/en/latest/>`_.

This demo has an implementation of a Python script called ``giza`` which
calculates the square of a given number.

"""

import argparse


def calc_square(number, verbosity):
    """
    Calculate the square of a given number.

    :param number: An integer number.
    :param verbosity: An integer value for output verbosity.
    :return: The square of number.
    """
    answer = number**2
    if verbosity >= 2:
        print "the square of {} equals {}".format(number, answer)
    elif verbosity >= 1:
        print "{}^2 == {}".format(number, answer)
    else:
        print answer
    return answer


def main():
    """
    A small wrapper that is used for running as a CLI Script.

    Examples:

    ::

        $ giza 2
        > 4

        $ giza -v 3
        > 3^2 == 9

        $ giza -vv 4
        > the square of 4 equals 16
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    calc_square(args.number, args.verbosity)
    

if __name__ == '__main__':
    main()
