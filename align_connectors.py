#      Python: 3.7.6
#   Kodierung: utf-8
""" """
from split_text import token_split


class Aligner():
    """ """

    def __init__(self, connectors, mode='naive'):
        self.connectors = connectors
        self.mode = mode

    def align(self, src_path, tgt_path):
        """Aims to align the connectors from two text files.

        Args:
            src_path(str): directory of the file in the source language (the
                           same as self.connectors).
            tgt_path(str): directory of the target file, where we're trying to
                           find equivalents of the connectors in the source
                           file.

        """
        if self.mode == 'naive':
            return self.__naive_align(src_path, tgt_path)

    def __naive_align(self, src_path, tgt_path):
        """ """
        alignments = dict()
        src_file = open(src_path, encoding='utf-8')
        tgt_file = open(tgt_path, encoding='utf-8')
        while True:
            try:
                src_line = next(src_file).casefold()
                tgt_line = next(tgt_file).casefold()
            except StopIteration:
                break
            src_tokens = token_split(src_line)
            tgt_tokens = token_split(tgt_line)
            token_id = 0
            for token in src_tokens:
                if token in self.connectors:
                    # target line shorter than source line
                    if token_id >= len(tgt_tokens):
                        # target line empty
                        if not tgt_tokens:
                            equivalent = ''
                        else:
                            equivalent = tgt_tokens[-1]
                    else:
                        equivalent = tgt_tokens[token_id]
                    if token not in alignments:
                        alignments[token] = {equivalent: 1}
                    elif equivalent not in alignments[token]:
                        alignments[token][equivalent] = 1
                    else:
                        alignments[token][equivalent] += 1
                token_id += 1
        src_file.close()
        tgt_file.close()
        return alignments


def main():
    obj1 = Aligner({'aber', 'doch', 'jedoch',
                    'allerdings', 'andererseits', 'hingegen'})
    print(obj1.align('test.de', 'test.en'))
    print(obj1.align('de-en/europarl-v7.de-en.de', 'de-en/europarl-v7.de-en.en'))


if __name__ == "__main__":
    main()
