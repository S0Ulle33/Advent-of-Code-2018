"""Runs all solutions."""
import pathlib
import importlib

if __name__ == '__main__':

    p = pathlib.Path('.')
    days = [day.name for day in p.iterdir() if day.is_dir()
            and day.name.startswith('Day')]

    for day in days:
        day_module = importlib.import_module(day + ".solution")
        print(f'--- {day} ---')
        day_module.main()
        print("=" * (len(day) + 8))
        print()
