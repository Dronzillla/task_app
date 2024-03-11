from pathlib import Path
import csv

from dates import from_str_to_date, from_str_to_time


def check_file_exists(fname: str) -> bool:
    # get current cwd
    cwd = Path.cwd()
    # Check if file with csv data exists
    if Path(cwd, fname).exists():
        return True
    return False


def read_csv(fname: str) -> list[dict]:
    # Read a file to a dictionary
    lines = []
    with open(fname, "r") as rfile:
        reader = csv.DictReader(rfile)
        for line in reader:
            lines.append(line)
    return lines


def main():
    fname = "tasks.csv"
    result = read_csv(fname)
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
