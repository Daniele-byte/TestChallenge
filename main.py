import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Do you like CAPITALIZED strings??? Here's a tool to capitalize them! Just put a string and it will be capitalized")
    parser.add_argument('N', type=int, help='how many strings??')
    return parser.parse_args()


def capitalize(string: str):
    return input_string.upper()


if __name__ == "__main__":
    args = parse_arguments()
    for _ in range(args.N):
        print("Please give me a string!!!!")
        input_string = input()
        capitalized_string = capitalize(input_string)
        print("Here is your CAPITALIZED string!!! Enjoy ur day!! :D")
        print(capitalized_string)
