"""Solution to Advent of Code 2018, Day 1: Chronal Calibration (https://adventofcode.com/2018/day/1)."""
import itertools
import pathlib


def part_one(nums):
    '''
    Question:
        Starting with a frequency of zero,
        what is the resulting frequency after all of the changes in frequency have been applied?

    Sums all the changes in frequency.
    '''
    return sum(nums)


def part_two(nums):
    '''
    Question:
        What is the first frequency your device reaches twice?

    Changes frequency and adds it to the set,
    until there is no change in length of it.
    '''

    frequencies = set()
    current_frequency = 0

    for n in itertools.cycle(nums):
        current_frequency += n

        old_len = len(frequencies)
        frequencies.add(current_frequency)
        new_len = len(frequencies)

        if old_len == new_len:
            return current_frequency


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    nums = [int(line) for line in input_file.open()]

    print(f'Part One: {part_one(nums)}')
    print(f'Part Two: {part_two(nums)}')


if __name__ == '__main__':
    main()
