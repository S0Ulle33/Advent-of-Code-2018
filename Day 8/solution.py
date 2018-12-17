"""Solution to Advent of Code 2018, Day 8: Memory Maneuver (https://adventofcode.com/2018/day/8."""
import pathlib


def part_one(numbers):
    '''
    Question:
        What is the sum of all metadata entries?

    Creates a master node that recursively creates all other nodes. Sums all
    metadata entries recursively.
    '''

    class Node():
        '''Class representing a node of the tree.'''

        def __init__(self, sequence):

            self.child_count = sequence[0]
            self.metadata_count = sequence[1]
            sequence = sequence[2:]
            self.childrens = []

            # Creates children's nodes and adds them to the list
            for _ in range(self.child_count):
                child_node = Node(sequence)
                self.childrens.append(child_node)
                sequence = sequence[child_node.get_size():]

            self.metadata = sequence[:self.metadata_count]

        def get_size(self):
            '''Calculates the size of the node and returns it.'''
            header = 2
            childrens_size = sum(children.get_size()
                                 for children in self.childrens)
            size = header + self.metadata_count + childrens_size

            return size

        def sum(self):
            '''Sums all metadata entries and returns it.'''
            return sum(self.metadata + [children.sum() for children in self.childrens])

    # Creates a master node, which in turn creates all the other nodes
    root_node = Node(numbers)

    # Gets the sum of all metadata entries
    sum_ = root_node.sum()

    return sum_


def part_two(numbers):
    '''
    Question:
        What is the value of the root node?

    Creates a master node that recursively creates all other nodes. Calculates
    a value according to the specified rules recursively.
    '''

    class Node():
        '''Class representing a node of the tree.'''

        def __init__(self, sequence):

            self.child_count = sequence[0]
            self.metadata_count = sequence[1]
            sequence = sequence[2:]
            self.childrens = []

            # Creates children's nodes and adds them to the list
            for _ in range(self.child_count):
                child_node = Node(sequence)
                self.childrens.append(child_node)
                sequence = sequence[child_node.get_size():]

            self.metadata = sequence[:self.metadata_count]

        def get_size(self):
            '''Calculates the size of the node and returns it.'''
            header = 2
            childrens_size = sum(children.get_size()
                                 for children in self.childrens)
            size = header + self.metadata_count + childrens_size

            return size

        def value(self):
            '''Calculates the value of a node and returns it.'''
            if self.childrens:
                value = 0
                for i in self.metadata:
                    index = i - 1
                    if index < len(self.childrens):
                        value += self.childrens[index].value()
            else:
                value = sum(self.metadata)

            return value

    # Creates a master node, which in turn creates all the other nodes
    root_node = Node(numbers)

    # Gets the value of the root node
    value = root_node.value()

    return value


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    numbers = [int(number) for number in input_file.read_text().split()]

    print(f'Part One: {part_one(numbers)}')
    print(f'Part Two: {part_two(numbers)}')


if __name__ == '__main__':
    main()
