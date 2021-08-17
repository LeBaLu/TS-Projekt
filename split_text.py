#    Python: 3.7.6
# Kodierung: utf-8
""" """
import re


def token_split(s):
    """ """
    seps = re.compile(r"\s|\.|,|/|\:|\?|!")
    tokens = [token for token in re.split(seps, s) if token]
    return tokens


def main():
    print(token_split('Aber i bim doch a deitscher!'))


if __name__ == "__main__":
    main()