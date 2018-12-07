"""Solution to Advent of Code 2018, Day 6: Chronal Coordinates (https://adventofcode.com/2018/day/6)."""
import operator
import pathlib
from collections import defaultdict


def part_one(coordinates):
    '''
    Question:
        What is the size of the largest area that isn't infinite?

    Iterates over each point in the grid (for each x and y in the range of
    maximum x and maximum y). Finds all manhattan distances between the current
    point and all coordinates. Value of the coordinate with the minimum
    manhattan distance in areas dict is increased by 1, and if the current
    point is extreme, then the coordinate is added to the infinite_coords set.
    Finds the largest area from all areas.
    '''

    def calculate_manhattan_distance(p, q):
        '''Calculates manhattan distance between 2 points and returns it.'''
        distance = abs(p[0] - q[0]) + abs(p[1] - q[1])
        return distance

    def find_all_distances(point):
        '''
        Finds all manhattan distances between a given point and coordinates.
        '''
        distances = []
        for coordinate in coordinates:
            distance = calculate_manhattan_distance(current_point, coordinate)
            distances.append((distance, coordinate))
        return distances

    def is_extreme(point):
        '''
        Returns True if given point is extreme, i.e. its x or y equals 0,
        or x equals maximum x, or y equals maximum y.
        '''
        if not isinstance(point, tuple):
            return False

        p_x = point[0]
        p_y = point[1]
        return not all((p_x, p_y)) or p_x == max_x or p_y == max_y

    max_x = max(coordinates, key=operator.itemgetter(0))[0]
    max_y = max(coordinates, key=operator.itemgetter(1))[1]

    # Dictionary containing the coordinate as a key and the number of points
    # that have the minimum manhattan distance to this coordinate as a value
    areas = defaultdict(int)

    # A set containing coordinates that have at least one minimum manhattan
    # distance with a point that is on the edge of grid, i.e. infinite
    # coordinates
    infinite_coords = set()

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            current_point = (x, y)

            # List containing tuples with a distance, between current point
            # and coordinate, and the coordinate itself
            distances = find_all_distances(current_point)
            distances.sort()

            # If there are no equal distances, i.e. point is not equally far
            # from two or more coordinates
            if distances[0][0] != distances[1][0]:
                # Coordinate that has the minimum manhattan distance to the
                # current point
                min_coordinate = distances[0][1]
                areas[min_coordinate] += 1

                # If current point is extreme, then the coordinate to which it
                # has the minimum manhattan distance is infinite, so we add
                # this coordinate to the infinite_coords set
                if is_extreme(current_point):
                    infinite_coords.add(min_coordinate)

    # Finds the largest area
    largest_area = max(area for coord, area in areas.items()
                       if coord not in infinite_coords)
    return largest_area


def part_two(coordinates):
    '''
    Question:
        What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

    Iterates over each point in the grid (for each x and y in the range of
    maximum x and maximum y). Finds all manhattan distances between the current
    point and all coordinates. If the sum of these distances is less that
    10,000 then add 1 to the size of the shared region.
    '''

    def calculate_manhattan_distance(p, q):
        '''Calculates manhattan distance between 2 points and returns it.'''
        distance = abs(p[0] - q[0]) + abs(p[1] - q[1])
        return distance

    def find_all_distances(point):
        '''
        Finds all manhattan distances between a given point and coordinates.
        '''
        distances = []
        for coordinate in coordinates:
            distance = calculate_manhattan_distance(current_point, coordinate)
            distances.append(distance)
        return distances

    manhattan_distance_limit = 10000
    max_x = max(coordinates, key=operator.itemgetter(0))[0]
    max_y = max(coordinates, key=operator.itemgetter(1))[1]
    shared_region_size = 0

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            current_point = (x, y)
            distances = find_all_distances(current_point)

            if sum(distances) < manhattan_distance_limit:
                shared_region_size += 1

    return shared_region_size


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
    coordinates = []
    for coordinate in input_file.read_text().splitlines():
        coordinates.append(tuple(map(int, coordinate.split(', '))))

    print(f'Part One: {part_one(coordinates)}')
    print(f'Part Two: {part_two(coordinates)}')


if __name__ == '__main__':
    main()
