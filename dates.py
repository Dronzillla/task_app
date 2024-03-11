from datetime import datetime


def from_str_to_date(date_str: str):
    format = "%Y-%m-%d"
    return datetime.strptime(date_str, format).date()


def from_str_to_time(time_str: str):
    format = "%H:%M"
    return datetime.strptime(time_str, format).time()


def main():
    str_date = "2024-02-24"
    print(from_str_to_date(str_date))
    time = "15:50"
    print(from_str_to_time(time))


if __name__ == "__main__":
    main()
