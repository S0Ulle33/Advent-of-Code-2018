"""Solution to Advent of Code 2018, Day 7: The Sum of Its Parts (https://adventofcode.com/2018/day/7."""
import pathlib


def part_one(instructions):
    '''
    Question:
        In what order should the steps in your instructions be completed?

    Gets the next available steps in the list as long as set of steps is full.
    The first element of this list is the next step, add it to the resulting order, remove it from set of steps.
    '''

    def get_next_steps(steps, sequence):
        '''
        Gets the current steps in the set and their sequence in the list.
        Returns next available steps.
        '''
        next_steps = []
        for step in steps:
            if all(successor != step for (_, successor) in sequence):
                next_steps.append(step)
        return next_steps

    # Set containing all steps
    steps = set()

    # List containing the preceding step and the following, e.g.
    # "Step P must be finished before step F can begin." -> [(P, F), ...]
    predecessor_successor = []

    for instruction in instructions:
        words = instruction.split()
        predecessor = words[1]
        successor = words[-3]
        predecessor_successor.append((predecessor, successor))
        steps.update(predecessor, successor)

    order = ''
    while steps:
        # Gets next available steps in the list, sorts it
        next_steps = get_next_steps(steps, predecessor_successor)
        next_steps.sort()

        # The first element of this list is the next step
        step = next_steps[0]
        order += step

        # Since this step is completed, we delete it from the set of all steps
        steps.remove(step)

        # Update our predecessor_successor list
        predecessor_successor = [(p, s) for (p, s)
                                 in predecessor_successor if p != step]

    return order


def part_two(instructions):
    '''
    Question:
        With 5 workers and the 60+ second step durations described above, how
        long will it take to complete all of the steps?

    Creates 5 workers. While set of the all steps is full, or any of the
    workers have a job, we iterate over our workers, check if they have a job,
    if not, then add it.
    '''

    class Worker:
        '''Worker class representing elf worker.'''

        def __init__(self):

            self.job = None
            self.remaining_time = 0

        def add_work(self, letter):
            '''Adds work and time for it accordingly.'''
            self.job = letter
            self.remaining_time = 60 + ord(letter) - ord('A')

        def do_work(self):
            '''Perfoms work by reducing the remaining time by 1 second.'''
            if self.job and self.remaining_time:
                self.remaining_time -= 1

    def get_next_steps(steps, sequence):
        '''
        Gets the current steps in the set and their sequence in the list.
        Returns next available steps.
        '''
        next_steps = []
        for step in steps:
            if all(successor != step for (_, successor) in sequence):
                next_steps.append(step)
        return next_steps

    # Set containing all steps
    steps = set()

    # List containing the preceding step and the following, e.g.
    # "Step P must be finished before step F can begin." -> [(P, F), ...]
    predecessor_successor = []

    for instruction in instructions:
        words = instruction.split()
        predecessor = words[1]
        successor = words[-3]
        predecessor_successor.append((predecessor, successor))
        steps.update(predecessor, successor)

    # Resulting time
    time = 0

    # Initializes workers and adds them to the list
    workers = [Worker() for _ in range(5)]

    # While set of the steps is full, or any of the workers have a job...
    while steps or any(worker.remaining_time > 0 for worker in workers):
        # Gets next available steps in the list, sorts it
        next_steps = get_next_steps(steps, predecessor_successor)
        next_steps.sort()

        # Iterates over workers
        for worker in workers:
            worker.do_work()

            # If worker job is completed...
            if worker.remaining_time == 0:
                if worker.job:
                    # Updates our predecessor_successor list if worker have job
                    predecessor_successor = [(p, s) for (p, s) in
                                             predecessor_successor
                                             if p != worker.job]
                if next_steps:
                    # Gets next step
                    step = next_steps.pop()

                    # Adds work to the current worker
                    worker.add_work(step)

                    # Removes this step from the set of all steps
                    steps.remove(step)

        # Since there is no need for time between steps, we simply add 1
        # second to the total time
        time += 1

    return time


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    instructions = [instruction.strip() for instruction in input_file.open()]

    print(f'Part One: {part_one(instructions)}')
    print(f'Part Two: {part_two(instructions)}')


if __name__ == '__main__':
    main()
