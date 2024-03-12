from dataclasses import dataclass, field
from datetime import datetime
from dates import from_str_to_date


@dataclass
class Task:
    id: str = field()
    content: str = field()
    priority: int = field()
    deadline: datetime = field()


@dataclass
class TaskManager:
    all: list["Task"] = field(default=[])
    ids = list[int] = field(default=[])

    def search_by_id(self, search_id: int) -> Task:
        for task in self.all:
            if task.id == search_id:
                return task

    def search_by_content(self, search_content: str) -> Task:
        for task in self.all:
            if task.content == search_content:
                return task

    def add_task(self, task):

        atask = Task()

        self.all.append(atask)

    def delete_task(self, content: str):
        task = self.search_by_content(content)
        self.all.remove(task)

    def update_task(self): ...

    def parse_task_from_stout(self, task: str):
        # --add "Do laundry" --priority 1 --deadline "2024-02-24 11:00"
        ...

    def show_current_list(self): ...

    def parse_command(self, line: list[str]) -> None:
        # Get user command
        command = line[0]

        # ['--add', 'Call grandma', '--priority', '2', '--deadline', '2024-12-28 22:50']
        if command == "--add":
            ...
        # ['--del', 'Do laundry']
        elif command == "--del":
            content = line[1]
            self.delete_task(content)
        # ['--edit', 'Call grandma', '--content', 'Call mom', '--priority', '3', '--deadline', '2024-02-25 23:00']
        elif command == "--edit":
            ...

    def parse_commands(self, commands: list): ...

    # Add all records to a list of task instances
    def parse_tasks_from_csv(self, tasks_from_csv: list[dict]) -> None:
        for task in tasks_from_csv:
            self.all.append(self.parse_task_from_csv(task))

    def parse_task_from_csv(self, task: dict) -> Task:
        return Task(
            id=task["id"],
            content=task["content"],
            priority=int(task["priority"]),
            deadline=from_str_to_date(task["deadline"]),
        )


def main(): ...


if __name__ == "__main__":
    main()
