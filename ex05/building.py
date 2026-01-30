import sys
import string

def parse() -> str:
    """
    Objective:
        Parse the command-line args or prompt the user for the text input
    Returns:
        str: returns the text to be analyzed
    Raises:
        AssertionError: if args are wrong, or if input is interrupted
    """
    args = sys.argv

    if len(args) == 1 or (len(args) == 2 and args[1] == ""):
        while True:
            try:
                text = input("What is the text to count?\n")
                if text:
                    break
                print("Please provide a text to count.")
            except (EOFError, KeyboardInterrupt):
                raise AssertionError("input was interrupted")
    elif len(args) == 2:
        text = args[1]
    else:
        raise AssertionError("more than one argument is provided")
    return text

def count(text: str) -> None:
    """
    Objective:
        Counts and prints character types from the text.
    Args:
        str: text to be analyzed
    """
    upper = lower = digit = space = punc = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in string.punctuation:
            punc += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main() -> int:
    """
    Objective:
        Main entry for the program
        Handle errors, input text and prints errors
    Returns:
        int: exit code status
    """
    try:
        text = parse()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    count(text)
    return 0

if __name__ == "__main__":
    sys.exit(main())