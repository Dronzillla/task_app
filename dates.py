from datetime import datetime


def from_str_to_date(date_str: str):
    format = "%Y-%m-%d %H:%M"
    return datetime.strptime(date_str, format)


def main():
    str_date = "2024-02-24 15:50"
    print(from_str_to_date(str_date))


if __name__ == "__main__":
    main()
