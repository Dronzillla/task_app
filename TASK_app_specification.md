## Task app (V)

Create a program where you can track a list of your tasks. With each task, you should be able to specify its name, priority, and deadline.
- You can keep track of your tasks inside a `tasks.txt` file which your program would constantly modify. You can use a simple text format but we recommend using JSON or CSV because it should be easier to work with it.
- You can implement your program that, once you run it, you can input your desired arguments using a CLI-like commands (similar to [Tank](#tank-exercise-d) exercise above)
- Alternatively, your application could benefit from [parsing arguments](https://docs.python.org/3/howto/argparse.html#argparse-tutorial). 
For example, you could run it as 
```bash
python todo.py --add "Do dishes" --priority 2 --deadline "2024-02-24 12:00"
```
where the words with `--` such as `--add` are called python program options and the words 
following those, such as `"Do dishes"` are the arguments. In this case, you would indicate 
that you like to _add_ the task "Do dishes" as a task.

For example, interaction with your application could look like this (this is using arguments, but similar idea would work for CLI applications):
```bash
>>> python todo.py --add "Do dishes" --priority 2 --deadline "2024-02-24 12:00"
Task added successfully! Here is the current list:
2. Do dishes. Due date: 2024-02-24 12:00
>>> python todo.py --add "Do laundry" --priority 1 --deadline "2024-02-24 11:00"
Task added successfully! Here is the current list:
1. Do laundry. Due date: 2024-02-24 11:00
2. Do dishes. Due date: 2024-02-24 12:00
>>> python todo.py --add "Call grandma" --priority 2 --deadline "2024-02-24 15:00"
Task added successfully! Here is the current list:
1. Do laundry. Due date: 2024-02-24 11:00
2. Do dishes. Due date: 2024-02-24 12:00
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --del "Do laundry"
Task deleted successfully! Here is the current list:
2. Do dishes. Due date: 2024-02-24 12:00
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --del
Latest task deleted successfully! Here is the current list:
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --edit "Call ganma" --name "Call mom" --priority 3 --deadline "2024-02-25 17:00"  
Unfortunately, "Call ganma" task currently does not exist. Try again!
Here is the current list of tasks:
2. Call grandma. Due date: 2024-02-24 15:00
>>> python todo.py --edit "Call grandma" --name "Call mom" --priority 3 --deadline "2024-02-25 17:00"  
Task edited successfully! Here is the current list:
3. Call mom. Due date: 2024-02-25 17:00
```