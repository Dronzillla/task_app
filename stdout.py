import re
from dates import from_str_to_date
import shlex


# split the string
def split_string(command: str) -> list:
    return shlex.split(command)


# Extract date
def extract_date(command: str) -> str:
    date = re.findall(r"^.+(\d\d\d\d-\d\d-\d\d \d\d:\d\d)\"$", command)
    return date[0]


# Check if date is valid
def valid_date(date: str) -> bool:
    str_date = extract_date(date)
    try:
        from_str_to_date(str_date)
        return True
    except ValueError:
        return False


def enter_command() -> list:
    command = input("Command: ")
    # Possible commands:
    # command = '--add "Call grandma" --priority 2 --deadline "2024-12-28 22:50"'
    # command = '--del "Do laundry"'
    # command = '--edit "Call grandma" --content "Call mom" --priority 3 --deadline "2024-02-25 23:00"'

    # Verify del command
    # --del "Do laundry"
    if re.search(r"^--del \"[a-zA-z\s]+\"$", command) is not None:
        return split_string(command)

    # Verify add command
    # --add "Call grandma" --priority 2 --deadline "2024-02-24 15:00"
    if (
        re.search(
            r"^--add \"[a-zA-z\s]+\" --priority [12345] --deadline \"\d\d\d\d-\d\d-\d\d \d\d\:\d\d\"$",
            command,
        )
        is not None
    ):

        # Validate date
        if valid_date(command) == True:
            return split_string(command)

    # Verify edit command
    # --edit "Call grandma" --content "Call mom" --priority 3 --deadline "2024-02-25 17:00"
    if (
        re.search(
            r"--edit \"[a-zA-z\s]+\" --content \"[a-zA-z\s]+\" --priority [12345] --deadline \"\d\d\d\d-\d\d-\d\d \d\d\:\d\d\"$",
            command,
        )
        is not None
    ):
        # Validate date
        if valid_date(command) == True:
            return split_string(command)

    # Return None if none of conditions are met
    return None


def main() -> list[str]:
    command = enter_command()
    return command


if __name__ == "__main__":
    main()
