from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: str = field()
    task: str = field()
    priority: int = field()
    deadline: datetime = field()
    time: datetime = field()


@dataclass
class TaskManager:
    all: list["Task"] = field(default=[])

    # "Id": line["Id"],
    # "Task": line["Task"],
    # "Priority": int(line["Priority"]),
    # "Deadline": from_str_to_date(line["Deadline"]),
    # "Time": from_str_to_time(line["Time"]),


def main(): ...


if __name__ == "__main__":
    main()
