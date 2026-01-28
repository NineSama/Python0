import sys

def parse() -> int:
    args = sys.argv

    if len(args) == 1:
        raise ValueError()
    elif len(args) > 2:
        raise AssertionError("more than one argument is provided")

    data = args[1]
    try:
        number = int(data)
    except ValueError:
        raise AssertionError("argument is not an integer")

    return number

def is_odd_or_even(number: int) -> None:
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

        
def main() -> int:
    try:
        number = parse()
    except ValueError:
        return 1
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    is_odd_or_even(number)
    return 0


if __name__ == "__main__":
    sys.exit(main())