"""Solution to Advent of Code 2018, Day 2: Inventory Management System (https://adventofcode.com/2018/day/2)."""
import collections
import itertools
import pathlib


def part_one(list_of_ids):
    '''
    Question:
        What is the checksum for your list of box IDs?

    Produces a checksum by multiplying how many of IDs contains a letter which appears twice and three times.
    '''

    ntimes = {2: 0, 3: 0}
    for id_ in list_of_ids:
        letter_ntimes = {}
        collections._count_elements(letter_ntimes, id_)
        ntimes_set = set(list(letter_ntimes.values()))
        ntimes_set.discard(1)
        collections._count_elements(ntimes, ntimes_set)
    checksum = ntimes[2] * ntimes[3]
    return checksum


def part_two(list_of_ids):
    '''
    Question:
            What letters are common between the two correct box IDs?

    Finds common letters by removing the different character from either ID,
    that differ by exactly one character(e.g., 'fghij' and 'fguij').
    '''

    def differ_by_one_letter(s1, s2):
        '''Compares two strings, returns True if they differ by 1 letter.'''
        already_diffrent = False

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if already_diffrent:
                    return False
                else:
                    already_diffrent = True

        return True

    def common_letters(s1, s2):
        '''
        Returns common letters between two strings by removing differing character from first string.

        Example:
            a = 'abcdef1g'
            b = 'abcdef2g'
            print(common_letters(a, b))
            'abcdefg'
        '''
        for index, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                return s1[:index] + s1[index + 1:]

    for s1, s2 in itertools.combinations(list_of_ids, 2):
        are_different = differ_by_one_letter(s1, s2)
        if are_different:
            common_letters = common_letters(s1, s2)
            return common_letters


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    ids = [line.strip() for line in input_file.open()]

    print(f'Part One: {part_one(ids)}')
    print(f'Part Two: {part_two(ids)}')


if __name__ == '__main__':
    main()
