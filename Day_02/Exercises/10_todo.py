tasks = []

# Add new task at the end of the tasks
def create(tasks: list[str], task: str):
       tasks.append(task)

# Return the task in the index given
def read(tasks: list[str], index: int) -> str:
        return tasks[index]

# Change the value in the index to the new task
def update(tasks: list[str], index: int, new_task: str):
        tasks[index] = new_task

# Remove the task in the given index
def delete(tasks: list[str], index: int):
    tasks.pop(index)

# Sample Program Given
create(tasks, "Buy milk")
create(tasks, "Do homework")
create(tasks, "Sleep")
assert "Buy milk" in tasks
assert read(tasks, 1) == "Do homework"
update(tasks, 0, "Buy coffee")
assert "Buy milk" not in tasks
assert "Buy coffee" in tasks
delete(tasks, 2)
assert "Sleep" not in tasks
assert len(tasks) == 2


