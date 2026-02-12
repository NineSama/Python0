import sys
from ft_filter import ft_filter


def parse() -> tuple[str, int]:
    """
    Objective:
        Parse the command-line args
    Returns:
        tuple[str, int]: returns the string to be analyzed and the integer
    Raises:
        AssertionError: if arguments are wrong
    """
    args = sys.argv

    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    string = args[1]
    integer = args[2]

    try:
        integer = int(integer)
    except ValueError:
        raise AssertionError("the arguments are bad")
    return (string, integer)


def main() -> int:
    """
    Objective:
        Main entry for the program
        Handle errors, input text and prints errors
        Prints a list of words from a given str that have greater
        length than a given integer
    Returns:
        int: exit code status
    """
    try:
        string, integer = parse()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1

    result = ft_filter(lambda x: len(x) > integer, string.split())
    print(list(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
