"""Solution to Advent of Code 2018, Day 5: Alchemical Reduction (https://adventofcode.com/2018/day/5)."""
import pathlib
from string import ascii_lowercase


def part_one(polymer):
    '''
    Question:
        How many units remain after fully reacting the polymer you scanned?

    Performs a reaction on the polymer, gets the remaining units in list.
    Result is the length of that list.
    '''

    def can_react(unit1, unit2):
        '''
        Returns True if given units are same type and have opposite polarities.

        >>>can_react('a', 'A')
        True
        >>>can_react('a', 'B')
        False
        '''

        def same_type(unit1, unit2):
            '''
            Returns True if given units are same type.

            >>>same_type('e', 'E')
            True
            >>>same_type('e', 'c')
            False
            '''

            return unit1.lower() == unit2.lower()

        def opposite_polarity(unit1, unit2):
            '''
            Returns True if given units are same type.

            >>>opposite_polarity('e', 'E')
            True
            >>>opposite_polarity('e', 'e')
            False
            '''

            return ((unit1.isupper() and unit2.islower()) or
                    (unit1.islower() and unit2.isupper()))

        return (same_type(unit1, unit2) and
                opposite_polarity(unit1, unit2))

    def do_reaction(polymer):
        '''
        Reacts the polymer, returns remaining units.

        dabAcCaCBAcCcaDA  The first 'cC' is removed.
        dabAaCBAcCcaDA    This creates 'Aa', which is removed.
        dabCBAcCcaDA      Either 'cC' or 'Cc' are removed.
        dabCBAcaDA        No further actions can be taken.
        '''

        remaining_units = []

        for unit in polymer:
            if remaining_units and can_react(unit, remaining_units[-1]):
                remaining_units.pop()
            else:
                remaining_units.append(unit)

        return remaining_units

    # Performs a reaction and gets the remaining units
    units = do_reaction(polymer)
    # Returns how many units remaining
    return len(units)


def part_two(polymer):
    '''
    Question:
        What is the length of the shortest polymer you can produce by removing
        all units of exactly one type and fully reacting the result?

    For each reagent (letter) in reagents (lowercase alphabet) removes units of
    this reagent (lower and upper cases of that letter), performs a reaction
    and adds length of that reaction to a list. Finally, the result is the
    length of the shortest polymer (minimum length in list).
    '''

    def can_react(unit1, unit2):
        '''
        Returns True if given units are same type and have opposite polarities.

        >>>can_react('a', 'A')
        True
        >>>can_react('a', 'B')
        False
        '''

        def same_type(unit1, unit2):
            '''
            Returns True if given units are same type.

            >>>same_type('e', 'E')
            True
            >>>same_type('e', 'c')
            False
            '''

            return unit1.lower() == unit2.lower()

        def opposite_polarity(unit1, unit2):
            '''
            Returns True if given units are same type.

            >>>opposite_polarity('e', 'E')
            True
            >>>opposite_polarity('e', 'e')
            False
            '''

            return ((unit1.isupper() and unit2.islower()) or
                    (unit1.islower() and unit2.isupper()))

        return (same_type(unit1, unit2) and
                opposite_polarity(unit1, unit2))

    def do_reaction(polymer):
        '''
        Reacts the polymer, returns remaining units.

        dabAcCaCBAcCcaDA  The first 'cC' is removed.
        dabAaCBAcCcaDA    This creates 'Aa', which is removed.
        dabCBAcCcaDA      Either 'cC' or 'Cc' are removed.
        dabCBAcaDA        No further actions can be taken.
        '''

        remaining_units = []

        for unit in polymer:
            if remaining_units and can_react(unit, remaining_units[-1]):
                remaining_units.pop()
            else:
                remaining_units.append(unit)

        return remaining_units

    def remove_units(polymer, unit):
        '''Removes all units of one type from polymer and returns it.'''
        edited_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
        return edited_polymer

    # Set of reagents (alphabet in lowercase)
    reagents = set([c for c in ascii_lowercase])

    polymers_length = []
    # Removes all units of exactly one type and fully reacts the result and
    # adds its length to polymers_length list
    for reagent in reagents:
        edited_polymer = remove_units(polymer, reagent)
        reacted_polymer = do_reaction(edited_polymer)
        polymers_length.append(len(reacted_polymer))

    # Gets length of the shortest polymer
    shortest_polymer_length = min(polymers_length)
    return shortest_polymer_length


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    polymer = input_file.read_text().strip()

    print(f'Part One: {part_one(polymer)}')
    print(f'Part Two: {part_two(polymer)}')


if __name__ == '__main__':
    main()
