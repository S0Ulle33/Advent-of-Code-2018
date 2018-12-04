"""Solution to Advent of Code 2018, Day 4: Repose Record (https://adventofcode.com/2018/day/4)."""
import pathlib
from datetime import datetime
from collections import Counter, defaultdict


def part_one(records):
    '''
    Question:
        Find the guard that has the most minutes asleep. What is the ID of the
        guard you chose multiplied by the minute you chose?

    Iterates over records, parses time and guard action, then adds all minutes
    when guard was asleep as collections.Counter() object in guards dict.
    Finally finds ID of the guard that has the most minutes asleep and minute
    that guard spend asleep the most, and multiplies them.
    '''

    def get_datetime(record):
        '''Parses string of record and returns datetime object.'''

        # '[1518-05-30 00:04] ...' -> '1518-05-30 00:04'
        date_time_string = record.split('] ')[0].lstrip('[')
        # '1518-05-30 00:04' -> datetime.datetime(1518, 5, 30, 0, 4)
        date_time = datetime.strptime(date_time_string, '%Y-%m-%d %H:%M')
        return date_time

    def get_guard_id(record):
        '''Parses string of record and returns guard ID.'''

        # '[1518-05-30 00:04] Guard #2417 begins shift' -> '2417 begins shift'
        guard_action = record.split('#')[1]
        # '2417 begins shift' -> 2417
        guard_id = guard_action.split()[0]
        return guard_id

    # Because strings are in ISO-8601 format we can simply sort list directly,
    # without parsing it for dates to sort later
    records.sort()

    guards = defaultdict(Counter)

    for record in records:
        time = get_datetime(record)
        if '#' in record:
            guard_id = get_guard_id(record)
        elif 'falls' in record:
            fell_asleep_time = time
        elif 'wakes' in record:
            woke_up_time = time
            minutes = []
            for minute in range(fell_asleep_time.minute, woke_up_time.minute):
                minutes.append(minute % 60)
            guards[guard_id].update(Counter(minutes))

    # Total minutes asleep of each guard
    total_minutes_asleep = []
    for guard_id, counter in guards.items():
        total_minutes_asleep.append((sum(counter.values()), guard_id))

    # ID of the guard that has the most minutes asleep
    _, guard_id = max(total_minutes_asleep)

    # Minute that guard spend asleep the most
    minute = guards[guard_id].most_common()[0][0]

    # ID of the guard that has the most minutes asleep multiplied by the minute
    # that he spends asleep the most
    result = int(guard_id) * minute

    return result


def part_two(records):
    '''
    Question:
        Of all guards, which guard is most frequently asleep on the same minute?
        What is the ID of the guard you chose multiplied by the minute you chose?

    Iterates over records, parses time and guard action, then adds all minutes
    when guard was asleep as collections.Counter() object in guards dict.
    Finally of all guards, finds which guard is most frequently asleep on the
    same minute, that minute, and multiplies them.
    '''

    def get_datetime(record):
        '''Parses string of record and returns datetime object.'''

        # '[1518-05-30 00:04] ...' -> '1518-05-30 00:04'
        date_time_string = record.split('] ')[0].lstrip('[')
        # '1518-05-30 00:04' -> datetime.datetime(1518, 5, 30, 0, 4)
        date_time = datetime.strptime(date_time_string, '%Y-%m-%d %H:%M')
        return date_time

    def get_guard_id(record):
        '''Parses string of record and returns guard ID.'''

        # '[1518-05-30 00:04] Guard #2417 begins shift' -> '2417 begins shift'
        guard_action = record.split('#')[1]
        # '2417 begins shift' -> 2417
        guard_id = guard_action.split()[0]
        return guard_id

    # Because strings are in ISO-8601 format we can simply sort list directly,
    # without parsing it for dates to sort later
    records.sort()

    guards = defaultdict(Counter)

    for record in records:
        time = get_datetime(record)
        if '#' in record:
            guard_id = get_guard_id(record)
        elif 'falls' in record:
            fell_asleep_time = time
        elif 'wakes' in record:
            woke_up_time = time
            minutes = []
            for minute in range(fell_asleep_time.minute, woke_up_time.minute):
                minutes.append(minute % 60)
            guards[guard_id].update(Counter(minutes))

    # Most frequently asleep minute of each guard
    most_asleep_minutes = []
    for guard_id, counter in guards.items():
        most_asleep_minutes.append((counter.most_common()[0][::-1], guard_id))

    # Most frequently asleep minute and guard ID that most frequently asleep on
    # that minute
    (_, minute), guard_id = max(most_asleep_minutes)

    # ID of the guard that is most frequently asleep on the same minute
    # multiplied by that minute
    result = int(guard_id) * minute

    return result


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    records = [record.strip() for record in input_file.open()]

    print(f'Part One: {part_one(records)}')
    print(f'Part Two: {part_two(records)}')


if __name__ == '__main__':
    main()
