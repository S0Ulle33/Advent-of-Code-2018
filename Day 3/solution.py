"""Solution to Advent of Code 2018, Day 3: No Matter How You Slice It (https://adventofcode.com/2018/day/3)."""
import re
import pathlib
from collections import defaultdict


def part_one(claims):
    '''
    Question:
        How many square inches of fabric are within two or more claims?

    Counts how many times each inch has been claimed, then finds square inches
    of fabric that are within two or more claims.
    '''

    def get_claim_data(claim_str):
        '''
        Parses claim string and returns its x, y, width, height.

        Example:
            claim_str = "#3 @ 1,3: 4x4"
            print(get_claim_data(claim_str))
            1, 3, 4, 4
        '''
        _, x, y, width, height = map(int, re.findall(r'\d+', claim_str))
        return x, y, width, height

    def claimed_inches(x, y, width, height):
        '''
        Generator that yields all inches claimed by given input.

        Example:
            # x = 1, y = 3, width = 2, height = 2
            claimed = (1, 3, 2, 2)
            for inch in claimed_inches(*claimed):
                print(inch)
            (1, 3)
            (1, 4)
            (2, 3)
            (2, 4)
        '''
        for x_i in range(width):
            for y_i in range(height):
                yield (x + x_i, y + y_i)

    # Counts how many times each inch has been claimed
    overlaps = defaultdict(int)
    for claim in claims:
        x, y, width, height = get_claim_data(claim)
        for inch in claimed_inches(x, y, width, height):
            overlaps[inch] += 1

    # Finds square inches of fabric that are in two or more claims
    total_overlaps = len(
        [times for inch, times in overlaps.items() if times > 1])
    return total_overlaps


def part_two(claims):
    '''
    Question:
        What is the ID of the only claim that doesn't overlap?

    Counts how many times each inch has been claimed, then finds ID of claims
    that has overlap, and finally finds ID of claim that doesn't overlap by
    subtracting from all claim IDs overlap claim IDs.
    '''

    def get_claim_data(claim_str):
        '''
        Parses claim string and returns its id, x, y, width, height.

        Example:
            claim_str = "#1 @ 1,3: 4x4"
            print(get_claim_data(claim_str))
            1, 1, 3, 4, 4
        '''
        claim_id, x, y, width, height = map(int, re.findall(r'\d+', claim_str))
        return claim_id, x, y, width, height

    def claimed_inches(x, y, width, height):
        '''
        Generator that yields all inches claimed by given input.

        Example:
            # x = 1, y = 3, width = 2, height = 2
            claimed = (1, 3, 2, 2)
            for inch in claimed_inches(*claimed):
                print(inch)
            (1, 3)
            (1, 4)
            (2, 3)
            (2, 4)
        '''
        for x_i in range(width):
            for y_i in range(height):
                yield (x + x_i, y + y_i)

    # Counts how many times each inch has been claimed
    overlaps = defaultdict(int)
    for claim in claims:
        _, x, y, width, height = get_claim_data(claim)
        for inch in claimed_inches(x, y, width, height):
            overlaps[inch] += 1

    # Finds ID of claims that has overlap
    all_claims = {claim_id for claim_id, *_ in map(get_claim_data, claims)}
    overlap_claims = set()
    for claim in claims:
        claim_id, x, y, width, height = get_claim_data(claim)
        for inch in claimed_inches(x, y, width, height):
            if overlaps[inch] > 1:
                overlap_claims.add(claim_id)

    # Finds ID of claim that doesn't overlap
    result = all_claims - overlap_claims
    return result.pop()


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    claims = [line.strip() for line in input_file.open()]

    print(f'Part One: {part_one(claims)}')
    print(f'Part Two: {part_two(claims)}')


if __name__ == '__main__':
    main()
