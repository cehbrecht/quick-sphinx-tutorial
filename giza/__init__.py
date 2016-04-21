import argparse


def calc_square(number, verbosity=0):
    """
    Calculate the square of given number.

    :param number: An integer number.
    :param verbosity: An integer value for verbosity.
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


def run_main():
    """
    A small wrapper that is used for running as a CLI Script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    calc_square(args.number, args.verbosity)
    

if __name__ == '__main__':
    run_main()
