import sys


def parse() -> str:
    """
    Objective:
        Parse the command-line args
    Returns:
        str: returns the string to be encrypted
    Raises:
        AssertionError: if arguments are wrong
    """
    args = sys.argv

    if len(args) != 2:
        raise AssertionError("the arguments are bad")

    text = args[1]
    if not isinstance(text, str):
        raise AssertionError("the arguments are bad")
    return text


def encrypt(text: str) -> str:
    """
    Objective:
        Encrypts ever char from a given str to the morse
        equivalent found in NESTED_MORSE
    Return:
        str: an encrypted str in morse code
    Raises:
        AssertionError: if arguments are wrong
    """
    NESTED_MORSE = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/ "
    }
    encrypted_morse = ""
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        encrypted_morse += NESTED_MORSE[char]
    return (encrypted_morse.rstrip())


def main() -> int:
    """
    Objective:
        Main entry for the program
        Handle errors, input text and prints errors
        Sens input to encrypt function, and prints the result
    Returns:
        int: exit code status
    """
    try:
        text = parse()
        result = encrypt(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
